# part1 : 
def part1(initialOrder = "784235916"):
    order = list(initialOrder)
    for i in range(len(order)):
        order[i] = int(order[i])
    
    maxCup = max(order)
    index = 0
    l = len(order)
    curCup = order[0]
    nextCurCup = order[0]
    for turn in range(5):
        curCup = nextCurCup

        index = order.index(curCup)
        n1 = (index + 1) % l
        n2 = (index + 2) % l
        n3 = (index + 3) % l

        c1 = order[n1]
        c2 = order[n2]
        c3 = order[n3]

        order.remove(c1)
        order.remove(c2)
        order.remove(c3)

        nextCurCup = order[(order.index(curCup) + 1) % len(order)]
        
        destCup = curCup - 1
        while((destCup not in order) and (destCup > 0)):
            destCup -= 1
        if destCup == 0:
            destCup = maxCup
            while destCup not in order:
                destCup -= 1

        destIndex = order.index(destCup)

        order = order[:destIndex + 1] + [c1, c2, c3] + order[destIndex + 1:]
        print(order)

    print(order)

"""
PART 2 SOLUTION NOT MY OWN
SOURCE: unknown
"""
from itertools import chain

def p2(dumb = "784235916", **_):
    gen = f(chain(map(int, dumb), range(10, 1000001)), 10000000)
    return next(gen) * next(gen)

def f(x, n):
    prev = None
    d = {}
    for i in x:
        if prev is None:
            start = i
        else:
            d[prev] = i
        prev = i
    d[i] = start
    current = start
    length = len(d)
    for _ in range(n):
        a = d[current]
        b = d[a]
        c = d[b]
        next_ = d[c]
        d[current] = next_
        dest = current
        while True:
            dest -= 1
            if not dest:
                dest = length
            if dest not in (a, b, c):
                break
        d[c] = d[dest]
        d[dest] = a
        current = next_
    current = 1
    while d[current] != 1:
        current = d[current]
        yield current
