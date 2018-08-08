# Queues are used to provide more control over communication between processes
# any picklable object can be sent into a queue, 
# but pickling can be quite costly,
# so such objects should be kept small

# This engine scans all files in current direcotry in parallel
# one process is constructed for each core on the CPU
# each instructed to load some of the files into memory


def search(paths, query_q, results_q):
    '''
    This function runs in different (cpu_count()) processes
    paths: path.path
    query_q: multiprocessing.Queue, incoming queries
    results_q: multiprocessing.Queue, outgoing results
    '''
    lines = []
    for path in paths:  # load all texts to be searched in memory
        lines.extend(l.strip() for l in path.open())

    query = query_q.get()  # query init (unpickle)
    while query:
        results_q.put([l for l in lines if query in l])  # search line by line, put matching lines in results_q (pickle)
        query = query_q.get()  # query ctn'd (unpickle)


if __name__ == '__main__':
    from multiprocessing import Process, Queue, cpu_count  # guarded by `if`: not required in subprocesses
    from path import Path  # guarded by `if`: not required in subprocesses
    cpus = cpu_count()
    pathnames = [f for f in Path('.').listdir() if f.isfile()]
    paths = [pathnames[i::cpus] for i in range(cpus)]
    # paths is a list, having `cpus` elements,
    # each paths element is a list, sliced from pathnames list, 
    # each paths element list takes every `cpus`:th element from pathnames list,
    # each paths element list starts from 1st, 2nd, ..., cpus:th elelemt of pathnames list
    query_queues = [Queue() for p in range(cpus)]  # init query queues
    result_queue = Queue()  # init result queue, only one, all subs put data here, aggregated in main process

    search_procs = [
        Process(target=search, args=[p, q, result_queue])
        for p, q in zip(paths, query_queues)
        # p: paths element list, a sub set of file names in current directory
    ]
    for proc in search_procs:
        proc.start()

    # Above are initializations, following code starts the actual searching actions
    for q in query_queues:
        q.put('def')
        q.put(None)  # signal process termination
    for i in range(cpus):  # real time display
        for match in result_queue.get():
            print(match)
    for proc in search_procs:
        proc.join()  # wait, wait...

# This search engine is a start point for a distributed system
# Imagine if the searches were to sent out to multiple computers and then recombined
# `multiprocessing.Manager` manages subprocesses on remote systems
# to construct rudimentary distributed application
# For further reading, check the Python multiprocessing documentation

# For multiprocessing, the main drawback is that sharing data between processes is very costly
# excessively pickling objects quickly dominates processing time

# Multiprocessing works best if small amounts of data is required to be shared between processes,
# and a tremendous amount of work needs to be done on each one of the
# But if no data sharing is required,
# then it is more sensible just to start several different processes, have them work independantly

# NEVER share variables between processes!
# for shared vars will get overwritten, and other processes still keeps the old value
# this is very confusing to maintain, so don't do it.
