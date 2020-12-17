# mX : returns (min, max) representing the min and max x-coordinates for the
#      next cycle of cubes
def mX(cubes):
    allX = []
    for cube in cubes:
        allX.append(cube[0])
    return (min(allX) - 1, max(allX) + 1)

# mY : returns (min, max) representing the min and max y-coordinates for the
#      next cycle of cubes
def mY(cubes):
    allY = []
    for cube in cubes:
        allY.append(cube[1])
    return (min(allY) - 1, max(allY) + 1)

# mZ : returns (min, max) representing the min and max z-coordinates for the
#      next cycle of cubes
def mZ(cubes):
    allZ = []
    for cube in cubes:
        allZ.append(cube[2])
    return (min(allZ) - 1, max(allZ) + 1)

# mW : returns (min, max) representing the min and max w-coordinates for the
#      next cycle of cubes
def mW(cubes):
    allW = []
    for cube in cubes:
        allW.append(cube[3])
    return (min(allW) - 1, max(allW) + 1)

# near3 : returns neighbors of input cube in 3D space
def near3(cube):
    res = []
    for x in range(cube[0] - 1, cube[0] + 2):
        for y in range(cube[1] - 1, cube[1] + 2):
            for z in range(cube[2] - 1, cube[2] + 2):
                tmp = (x, y, z)
                if tmp != cube:
                    res.append(tmp)
    return res

# activeN3 : returns number of active neighbors of input cube in 3D space
def activeN3(cube, d):
    ns = near3(cube)
    active = 0
    for x in ns:
        if x in d:
            if d[x] == 1:
                active += 1
    return active

# near4 : returns neighbors of input cube in 4D space
def near4(cube):
    res = []
    for x in range(cube[0] - 1, cube[0] + 2):
        for y in range(cube[1] - 1, cube[1] + 2):
            for z in range(cube[2] - 1, cube[2] + 2):
                for w in range(cube[3] - 1, cube[3] + 2):
                    tmp = (x, y, z, w)
                    if tmp != cube:
                        res.append(tmp)
    return res

# activeN4 : returns number of active neighbors of input cube in 4D space
def activeN4(cube, d):
    ns = near4(cube)
    active = 0
    for x in ns:
        if x in d:
            if d[x] == 1:
                active += 1
    return active

# unique : returns unique elements of input array
def unique(arr):
    for x in arr:
        if arr.count(x) == 1:
            continue
        else:
            for i in range(arr.count(x) - 1):
                arr.remove(x)
    return arr

# part1 : 3D cube set, return count of active neighbors after 6 cycles
def part1():
    with open("Day 17 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    allCubes = []
    aCubes = []
    iCubes = []
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            allCubes.append((x, y, 0))
            if lines[y][x] == "#":
                aCubes.append((x, y, 0))
            else:
                iCubes.append((x, y, 0))

    # d is a dictionary which stores ALL cubes
    d = dict()
    
    for x in range(mX(allCubes)[0] - 6, mX(allCubes)[1] + 6 + 1):
        for y in range(mY(allCubes)[0] - 6, mY(allCubes)[1] + 6 + 1):
            for z in range(- 6, 6 + 1):
                if (x, y, z) in aCubes:
                    d[(x, y, z)] = 1
                else:
                    d[(x, y, z)] = 0

    for cycle in range(1, 7):
        aCubes = []
        for cube in d:
            if d[cube] == 1:
                if activeN3(cube, d) in [2,3]:
                    aCubes.append(cube)
            else:
                if activeN3(cube, d) == 3:
                    aCubes.append(cube)
        for cube in d:
            if cube in aCubes:
                d[cube] = 1
            else:
                d[cube] = 0

    count = 0
    for cube in d:
        if d[cube] == 1:
            count += 1

    return count

# part2 : 4D cube set, return count of active neighbors after 6 cycles
def part2():
    with open("Day 17 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    allCubes = []
    aCubes = []
    iCubes = []
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            allCubes.append((x, y, 0, 0))
            if lines[y][x] == "#":
                aCubes.append((x, y, 0, 0))
            else:
                iCubes.append((x, y, 0, 0))

    # d is a dictionary which stores ALL cubes
    d = dict()
    
    for x in range(mX(allCubes)[0] - 6, mX(allCubes)[1] + 6 + 1):
        for y in range(mY(allCubes)[0] - 6, mY(allCubes)[1] + 6 + 1):
            for z in range(- 6, 6 + 1):
                for w in range(- 6, 6 + 1):
                    if (x, y, z, w) in aCubes:
                        d[(x, y, z, w)] = 1
                    else:
                        d[(x, y, z, w)] = 0

    for cycle in range(1, 7):
        aCubes = []
        for cube in d:
            if d[cube] == 1:
                if activeN4(cube, d) in [2,3]:
                    aCubes.append(cube)
            else:
                if activeN4(cube, d) == 3:
                    aCubes.append(cube)
        for cube in d:
            if cube in aCubes:
                d[cube] = 1
            else:
                d[cube] = 0

    count = 0
    for cube in d:
        if d[cube] == 1:
            count += 1

    return count

# main : runs and outputs both parts of the problem
def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
