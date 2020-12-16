# part1 : sum all values which are invalid for ALL ranges
def part1():
    with open("Day 16 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # get lines corresponding to my ticket and others' tickets
    for i in range(len(lines)):
        if lines[i] == "your ticket:":
            mine = i
        if lines[i] == "nearby tickets:":
            near = i

    # store each line of ranges as a list of valid numbers
    ranges = []
    for i in range(mine - 1):
        curr = lines[i]
        curRange = curr.split(": ")[1]
        curRange = curRange.split(" or ")
        tmpRange = []
        for r in curRange:
            tmp = r.split("-")
            start = int(tmp[0])
            stop = int(tmp[1])
            for j in range(start, stop + 1):
                tmpRange.append(j)
        ranges.append(tmpRange)

    res = 0

    # loop through each value of each nearby ticket and add to count if it is
    # invalid under ALL ranges
    for i in range(near + 1, len(lines)):
        # process each line of nearby tickets
        nearVals = lines[i].split(",")
        for j in range(len(nearVals)):
            nearVals[j] = int(nearVals[j])
        
        for val in nearVals:
            valid = 0
            for r in ranges:
                if val in r:
                    valid = 1
                    break
            if valid != 1:
                res += val

    print(res)
    return

# intersect : returns the intersection of two lists
def intersect(a1: list, a2: list) -> list:
    res = []
    for x in a1:
        if x in a2:
            res.append(x)
    return res

# allOne : checks if a dictionary (int:list)'s values are all of length 1
def allOne(d: dict) -> bool:
    for x in d:
        if len(d[x]) != 1:
            return False
    return True

# part2 : obtain unique mapping of field to position by removing all nearby
#         tickets which have no valid range (i.e. ticket MUST be invalid) and
#         comparing the remaining ones to all ranges. Then, return the product
#         of the values of my ticket corresponding to any of the first 6 fields
#         (which start with the word "departure")
def part2():
    with open("Day 16 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # get lines corresponding to my ticket and others' tickets
    for i in range(len(lines)):
        if lines[i] == "your ticket:":
            mine = i
        if lines[i] == "nearby tickets:":
            near = i

    # store each line of ranges as a list of valid numbers
    ranges = []
    for i in range(mine - 1):
        curr = lines[i]
        curRange = curr.split(": ")[1]
        curRange = curRange.split(" or ")
        tmpRange = []
        for r in curRange:
            tmp = r.split("-")
            start = int(tmp[0])
            stop = int(tmp[1])
            for j in range(start, stop + 1):
                tmpRange.append(j)
        ranges.append(tmpRange)

    # get invalid tickets
    invalid = []
    for i in range(near + 1, len(lines)):
        nearVals = lines[i].split(",")
        for j in range(len(nearVals)):
            nearVals[j] = int(nearVals[j])
        for val in nearVals:
            valid = 0
            for r in ranges:
                if val in r:
                    valid = 1
                    break
            if valid != 1:
                invalid.append(lines[i])
                break

    # remove all invalid tickets from list
    for x in invalid:
        lines.remove(x)

    # d is a dictionary where keys are positions and values are a list of fields
    # for which that position is in a valid range
    d = dict()

    # obtain the mapping by intersecting the set of valid fields as we traverse
    # through the list of nearby tickets and check for validity since, for each
    # position, the intersection of valid fields is the largest possible set of
    # fields which makes all nearby tickets valid
    for i in range(near + 1, len(lines)):
        nearVals = lines[i].split(",")
        for j in range(len(nearVals)):
            nearVals[j] = int(nearVals[j])
        for j in range(len(nearVals)):
            tmp = []
            for k in range(len(ranges)):
                if nearVals[j] in ranges[k]:
                    tmp.append(k)

            if j in d:
                d[j] = intersect(d[j], tmp)
            else:
                d[j] = tmp

    # assuming the input was valid, we can repetitively find positions which are
    # mapped to a single field, and remove that field from all other positions'
    # possible mappings. This will leave a unique position-field mapping.
    while(not allOne(d)):
        for x in d:
            if len(d[x]) == 1:
                for y in d:
                    if((y != x) and (d[x][0] in d[y])):
                        d[y].remove(d[x][0])

    # get indices of fields which start with "departure"
    startWithDeparture = []
    for i in range(mine - 1):
        curr = lines[i]
        if curr[0:len("departure")] == "departure":
            startWithDeparture.append(i)

    # obtain my ticket
    myTicket = lines[mine + 1].split(",")

    # multiply values in myTicket corresponding to fields in startWithDeparture
    res = 1
    for x in d:
        if d[x][0] in startWithDeparture:
            res *= int(myTicket[x])

    print(res)
    return
