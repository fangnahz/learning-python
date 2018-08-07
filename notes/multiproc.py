from multiprocessing import Process, cpu_count
import time
import os


class MuchCPU(Process):  # starts different processes, GIL does not limit Process, as it does threading.Thread
    def run(self):
        print(os.getpid())
        for _ignore in range(200000000):
            pass


if __name__ == '__main__':
    procs = [MuchCPU() for _ignore in range(cpu_count())]  # No reason to have more processes than cpu_count()
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print('work took {} seconds'.format(time.time() - t))
