# coding: utf-8
# [ This is an example of good code for stupid ideas
#   sorting as service is ridiculous,
#   sort_in_process() instead of sorted() is worse ]
# AsyncIO's futre library combines best of threads and processes
#   to handle I/O bound and CPU bound activities
# I/O bound: event loop
# CPU intensive: processes
import asyncio
import json
from concurrent.futures import ProcessPoolExecutor


def sort_in_process(data):
    # gnome/stupid sort
    # 1. good to have (reletively) expensive decoding on a different CPU
    nums = json.loads(data.decode())
    curr = 1
    while curr < len(nums):
        if nums[curr] >= nums[curr-1]:
            curr += 1
        else:
            nums[curr], nums[curr-1] = nums[curr-1], nums[curr]
            if curr > 1:
                curr -= 1
    # 2. pickled json strings generally smaller than pickled lists,
    #   good to have less data passing between processes
    return json.dumps(nums).encode()


# 3. two methods looked linear: illusion,
#   but no worries about shared memory or concurrency primitives
@asyncio.coroutine
def sort_request(reader, writer):
    print("Received connection")
    # 6. reading is potentially blocking, so have to use yield
    # 8. read(8) reads up to 8 bytes
    length = yield from reader.read(8)
    # 9. length is the number of bytes of data the client intends to send,
    #   so readexactly(length) (buffer until all recieved, or connection close)
    data = yield from reader.readexactly(int.from_bytes(length, 'big'))
    # 10. run_in_executor() to run futures,
    #   default to ThreadPoolExecutor,
    #   but can pass in a different executor,
    #   or...
    # 12. no boilerplate for using futures with AsyncIO,
    #   coroutine automatically wraps function call in a future
    #   and submits it to the executor
    # 13. code blocks until the future completes,
    #   while event loop continues in other processes with other connections, tasks or futures
    # 14. when future is done, coroutine wakes up and continues to write data back to the client
    result = yield from asyncio.get_event_loop().run_in_executor(None, sort_in_process, data)
    print("Sorted list")
    # 7. writing is putting data on a queue, non-blocking,
    #   which AsyncIO sends out in the background
    writer.write(result)
    writer.close()
    print("Connection closed")

# 15. It might be better to run multiple event loops in different processes,
#   but probably it is better to runing independent copies of a program with a single event loop,
#   than try to coordinate everything with a master multiporcessing process

loop = asyncio.get_event_loop()
# 11. set a different default when setting up the event loop
loop.set_default_executor(ProcessPoolExecutor())
# 4. start_server hooks into AsyncIO's streams,
#   while create_server uses transport/protocol,
#   so we can pass in a normal coroutine (sort_request) which receives a reader and writer param
#   instead of a protocol class,
#   these both represent streams of bytes
server = loop.run_until_complete(asyncio.start_server(sort_request, '127.0.0.1', 2015))
print("Sort Service running")

loop.run_forever()
server.close()
# 5. this is TCP server, not UDP, socket cleanup requires a bloking call,
#   so wait_closed coroutine is used on the event loop
loop.run_until_complete(server.wait_closed())
loop.close()
