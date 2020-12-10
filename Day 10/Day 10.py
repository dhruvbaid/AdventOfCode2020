# main : runs code for Day 10.
def main():
    # part 1
    with open("Day 10 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = int(lines[i].split("\n")[0])

    i = 0

    # for part 1, we need to use ALL the adapters, and we also want them to be
    # in increasing order, so we can just sort them
    arr = [0] + sorted(lines) + [max(lines) + 3]

    diff3 = 0
    diff1 = 0

    # arr2 stores this list of integers, but with dividors "D" at the points
    # where we know that there can be no swaps in part 2 (i.e. where the
    # difference between the intgers to the left and right is 3). This divides
    # our list into a disjoint union of sets which have invariant start and end
    # integers which we can then loop through much more efficiently, find the
    # number of valid permutations of each, multiply, and return the answer
    arr2 = []

    for i in range(len(arr) - 1):
        cur = arr[i]
        nex = arr[i+1]
        if nex-cur == 1:
            diff1 += 1
            arr2.append(cur)
        if nex-cur == 3:
            diff3 += 1
            arr2.append(cur)
            arr2.append("D")
    arr2.append(arr[-1])

    print(f"Part 1: {diff1 * diff3}")

    # part 2
    count = 1
    start = 0
    stop = 0
    for i in range(1, len(arr2) - 1):
        pre = arr2[i - 1]
        cur = arr2[i]
        nex = arr2[i + 1]
        if pre == "D":
            start = i
        if nex == "D":
            stop = i
            if start == 0:
                subset = arr2[:stop + 1]
                count = count * myCount(allPerms(subset))
                # print(f"{subset}: {myCount(allPerms(subset))}")
            else:
                subset = arr2[start : stop + 1]
                count = count * myCount(allPerms(subset))
                # print(f"{subset}: {myCount(allPerms(subset))}")
    print(f"Part 2: {count}")

# perm : returns all permutations of an input list, assuming distinct elements
def perm(arr: list):
    if len(arr) <= 1:
        return [arr]
    else:
        res = []
        for i in range(len(arr)):
            first = [arr[i]]
            if i == 0:
                rest = arr[1:]
            elif i == len(arr) - 1:
                rest = arr[:i]
            else:
                rest = arr[:i] + arr[i+1:]

            rPerms = perm(rest)
            for j in range(len(rPerms)):
                rPerms[j] = first + rPerms[j]
            res += rPerms
        return res

# unique : returns a list containing all unique elements of the input list
def unique(arr: list):
    res = []
    for x in arr:
        if x not in res:
            res.append(x)
    return res

# remove : returns a list comprising of all distinct (up to order) permutations
#          of the original list, with n elements removed
def remove(arr: list, n: int):
    res = []
    allPerms = perm(arr)
    for i in range(len(allPerms)):
        allPerms[i] = sorted(allPerms[i][n:])
    allPerms = unique(allPerms)
    return allPerms

# allPerms : given an input list, return all possible permutations of that list
#            which fix the first and last elements, including removing one or
#            all of the intermediate elements
def allPerms(arr: list):
    f = arr[0]
    l = arr[-1]
    b = arr[1:-1]
    res = []
    for rem in range(len(b) + 1):
        removed = remove(b, rem)
        for x in removed:
            rPerms = perm(x)
            for i in range(len(rPerms)):
                rPerms[i] = [f] + rPerms[i] + [l]
            res += rPerms
    return res

# isValid : given a list, check if it is in strictly increasing order with the
#           difference between 2 consecutive elements not being more than 3
def isValid(arr: list):
    for i in range(len(arr) - 1):
        cur = arr[i]
        nex = arr[i+1]
        if((nex - cur > 3) or (nex < cur)):
            # print(arr)
            return False
    return True

# myCount : given an input list of permutations, return their valid count. Note
#           that even if none of the permutations are valid, we still return 1
#           because eventually we are going to multiply our main count by this
#           number!
def myCount(arr: list):
    return max(1, sum([isValid(x) for x in arr]))
