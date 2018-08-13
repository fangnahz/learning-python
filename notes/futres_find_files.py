# coding: utf-8
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from os.path import sep as pathsep
from collections import deque


def find_files(path, query_string):  # run in separate thread (or process if using ProcessPoolExecutor)
    # this function does not access globals,
    # interactions is passed into or returned from it
    # This behavior is not required but is prefered
    # This provides a clean (easy to spot in case of problems) boundry between concurrencies
    # Accessing outside vars with synchronization,
    # otherwise race conditions occur:
    #  when two concurrencies read the same value, and both try to increment it by 1,
    #  thus the result is 1 less than the correct value.
    #  When sharing is must, use known-safe constructs such as queues to avoid racing
    subdirs = []
    for p in path.iterdir():
        full_path = str(p.absolute())
        # is_symlink() check is a lazy way for this demo to prevent infinite loops
        if p.is_dir() and not p.is_symlink():
            subdirs.append(p)
        if query_string in full_path:
            print(full_path)
    return subdirs

query = '.py'
futures = deque()
basedir = Path(pathsep).absolute()

# event loop, concurrency set to 10,
# for ProcessPoolExecutor usually set to cpu_count()
# for treading, each takes up some memory, so concurrency sould not be too high
# or else disk speed will very soon becomes the bottleneck
with ThreadPoolExecutor(max_workers=10) as executor:
    # enqueue dirs to search, starts when any worker is available
    # submit() immediately returns a Future object, enqueued (at the end of queue), which promises a result eventually
    futures.append(executor.submit(find_files, basedir, query))
    while futures:
        # loop removes first future from queue, indicating a (paralleled) breadth first search
        future = futures.popleft()
        if future.exception():
            # probably just a permission error
            # A real app should take this more seriously
            # If not dealt with here, it would raise when result() is called,
            # should then be handled with a try/catch block
            continue
        elif future.done():
            subdirs = future.result()
            for subdir in subdirs:
                # enqueue subdirs to search, starts when any worker is available
                futures.append(executor.submit(find_files, subdir, query))
        else:
            futures.append(future)
