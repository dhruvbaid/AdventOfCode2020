# part1 : given a startTime and a list of times when buses depart from the
#         station (starting at time 0), find the earliest bus which you can take
#         and return the bud ID multiplied by the time you had to wait for the
#         bus
def part1():
    with open("Day 13 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    startTime = int(lines[0])
    busTime = startTime
    times = lines[1].split(",")

    # ignore all x's
    while "x" in times:
        times.remove("x")

    for i in range(len(times)):
        times[i] = int(times[i])

    # start at startTime, increment one every loop and check if there are any
    # buses which come at that time; if so, return that bus ID * wait time
    while(True):
        for x in times:
            if busTime % x == 0:
                print((busTime - startTime) * x)
                return
        busTime += 1
    
# part2 : Find the earliest time such that the first bus ID departs at that time
#         and each subsequent listed bus ID departs at that subsequent minute
def part2():
    with open("Day 13 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    times = lines[1].split(",")

    # store a clean (x's removed) line 2 of input as a separate list (timesC)
    # and also keep a dictionary which is the index of each actual bus time in
    # the original input (which is equivalent to the offset time at which the
    # bus should arrive)
    timesC = []
    d = dict()
    for i in range(len(times)):
        if times[i] != "x":
            timesC.append(int(times[i]))
            d[int(times[i])] = i

    # we will start with the maximum variable, because that will minimize the
    # number of computations
    maxVar = max(timesC)

    # counts keeps track of whether or not the time we have right now is one
    # which allows for certain buses to arrive at their designated times
    counts = dict()
    for x in timesC:
        counts[x] = 0

    # since we are starting with maxVar, maxVar definitely arrives at the
    # correct time
    counts[maxVar] = 1
    
    res = maxVar

    # count keeps track of how much we can add to res at every iteration: the
    # idea is that if we have found a time which works for certain buses, then
    # we can add the LCM of those bus IDs to res to ensure that the next time
    # we iterate through also allows at least those buses to all arrive at
    # their designated times. Using LCM and not just product ensures that we
    # don't accidentally skip any times which may have been valid.
    count = maxVar

    # loop through possible times and check modularity
    while(True):
        valid = 1
        for x in timesC:
            # only check those bus IDs which have not already been accounted for
            if counts[x] == 0:
                if (((res - d[maxVar] + d[x]) % x) != 0):
                    valid = 0
                    break
                else:
                    # bus ID x is valid; account for it in counts and count
                    counts[x] = 1
                    count = 1

                    # I mentioned using LCM instead of a simple product above,
                    # but gcd(i,j) = 1 for any i,j in timesC (they are pirimes)
                    # and so the result of LCM is the same as a product
                    for a in counts:
                        if counts[a] == 1:
                            count *= a
        if valid == 1:
            print(res - d[maxVar])
            return
        else:
            res += count
