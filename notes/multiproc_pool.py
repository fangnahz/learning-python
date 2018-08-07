# use mulitprocessing pools to facilitate communicating processes, pools ...
# * restrict the number of places that code in different processes interact with each other
# * hide the process of passing data between processes (like a function call)
# * under the hood, objects in one process are been pickled and passed into a pipe,
# then another process retrieves data frome the pipe and unpickles it.
# Work is done in the subprocess and a result is produced.
# The result is pickled and passed into a pipe.
# Eventually, the original process unpickles it and returns it.)
import random
from multiprocessing.pool import Pool


def prime_factor(values):
    factors = []
    for divisor in range(2, value-1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor))
            factors.extend(prime_factor(quotient))
    else:
        factors = [value]
    return factors


if __name__ == '__main__':
    pool = Pool()  # defaults to create cpu_count() processes
    to_factor = [
        random.randint(100000, 50000000) for _ignored in range(20)
    ]
    # pool pickles each element in to_factor, pass to available process, which executes
    # when done, result is pickled and passed back to pool.
    # after all done, results is passed back to original process, which has been waiting
    # pools also have map_async method, which calls results.get() when done
    # async with other methods like ready() and wait()
    # also apply_async method to queue up jobs
    # pools can also be close(), then all further tasks are refused
    # or terminate(), which also ignores all waiting jobs in pool,
    # (but running jobs are allowed to complete.)
    results = pool.map(prime_factor, to_factor)
    for value, factors in zip(to_factor, results):
        print('The factors of {} are {}'.format(value, factors))
