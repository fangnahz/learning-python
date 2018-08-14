# coding: utf-8
# * AsyncIO: futures + event loop + coroutines + yield
#   Is designed for network I/O
#   coroutines: instead of threads, to avoid memory and other resources consumption
#   event loop: requires immediate return, so...
#   yield: return control to event loop instantly, used e.g. for blocking lib calls
import asyncio
import random


# 10. documents this coroutine is used as a future in an event loop
# 11. the functions in this module works without the decorator,
#   because 'yield' is used
# 12. but the decorator can also be used to wrap normal functions (that doesn't yield)
#   to fulfill the coroutine API so that event loop can handle them as a future,
#   although the function executes before returning control to event loop (will block)
# 13. coroutines run till next yield, then returns control to event loop,
#   event loop checks all child task, if any is ready,
#   event loop will pass the result to that coroutine, give it contol to execute,
#   until the next yield or return
#   (again, it is just standard coroutine behavior)
# 14. (takeaway) async enforces a synchronous style code,
#   we just explicitly wait for a result when needed,
#   the non-deterministic behavior of threads is removed,
#   so we don't have to worry about shared states
# 15. (takeaway) it's still a good idea to avoid accessing shared state from inside a coroutine,
#   because still there are some futures executed in threads under the hood,
#   stick to a 'share nothing' philosophy avoids a ton of difficult bugs
# 16. (takeaway) AsyncIO allows all sorts of stuff to happen inside the event loop,
#   but it collects logical sections of code together inside a single coroutine,
#   so itself looks like it's doing everythind in order,
#   (e.g. the `yield from asyncio.sleep(delay)` call in random_sleep)
#   this is the MAIN benefit of the AsyncIO module
@asyncio.coroutine
def random_sleep(counter):
    delay = random.random() * 5
    print(f"{counter} sleeps for {delay:.2f} seconds")
    yield from asyncio.sleep(delay)
    # 5. send control back to event loop (not five_sleepers)
    # 6. if any delay is less than the 2 seconds wait in five_sleepers,
    #   control will be passed back to the relevant future (in here),
    #   and the following print statement will be executed
    print(f"{counter} awakens")


@asyncio.coroutine
def five_sleepers():
    print("Creating five tasks")
    tasks = [asyncio.ensure_future(random_sleep(i)) for i in range(5)]  # coroutines
    # * asyncio.async is deprecated under 3.5, instead using asyncio.ensure_future
    # 3. adds tasks to loop's task queue for concurrent execution, when control is returned to event loop
    print("Sleeping after starting five tasks")
    yield from asyncio.sleep(2)
    # 4. pause five_sleepers for 2 seconds, but event loop task (random_sleep) executions keep going
    # 7. after sleep, executes to next yield (as a standard coroutine's behavior)
    print("Waking and waiting for five tasks")
    yield from asyncio.wait(tasks)
    # 8. waits for all futures in tasks queue to finish,
    #   after all futures finished, they are removed from task queue (on return)

asyncio.get_event_loop().run_until_complete(five_sleepers())  # coroutines
# 1. get_event_loop() gets event loop
# 2. run_until_complete run a future, five_sleepers here
#   deal with iteration, exception, function returns, parallel calls, etc.
# 9. now event loop is empty, run_until_complete terminates and program ends
print("Done five tasks")
