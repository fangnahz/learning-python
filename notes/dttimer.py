from datetime import datetime


def ttimer(ts0, ts1, num):
    t = sorted([ts0, ts1])
    t0 = datetime.strptime(t[0], '%H:%M:%S')
    t1 = datetime.strptime(t[1], '%H:%M:%S')
    dt = t1 - t0
    print('{} s'.format(dt.total_seconds()))
    print('{:.2f} /s'.format(num/dt.total_seconds()))


def dtimer(ts0, ts1, num):
    t = sorted([ts0, ts1])
    t0 = datetime.strptime(t[0], '%Y-%m-%d %H:%M:%S')
    t1 = datetime.strptime(t[1], '%Y-%m-%d %H:%M:%S')
    dt = t1 - t0
    print('{} s'.format(dt.total_seconds()))
    print('{:.2f} /s'.format(num/dt.total_seconds()))
