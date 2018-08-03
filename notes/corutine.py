# Corutines
import time


def player():
    val = 0
    while True:
        time.sleep(0.5)
        if val % 7:
            val = yield '', val
        else:
            val = yield 'pass', val
        val += 1


def game_start(max):
    players = (player(), player())
    for p in players:
        next(p)
    cnt = 0
    val = 0
    try:
        while cnt < max:
            for num, p in enumerate(players):
                cnt += 1
                seven, val = p.send(val)
                res = seven or val
                print('p%s: %s' % (num, res))
    finally:
        for p in players:
            p.close()
