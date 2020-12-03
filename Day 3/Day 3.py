# calc : actual computation of the number of trees encountered, given a 2D array
#	 representing the tree arrangement as well as the number of steps right
#	 and down taken each time
def calc(arr, r, d):
    count = 0
    col = 0
    row = 0
    ncols = len(arr[0])
    nrows = len(arr)
    while row < nrows - 1:
        col += r
        col = col % ncols
        row += d
        # print(f"{row},{col}")
        if arr[row][col] == "#":
            count += 1
    return count

# path1 : calculate number of trees encountered when taking a (3,1) path
def part1():
    arr = []
    with open("Day 3 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    count = 0
    for i in range(len(lines)):
        un = lines[i]
        if un[-1] == '\n':
            un = un[:-1]
        tmp = []
        for i in range(len(un)):
            tmp.append(un[i])
        arr.append(tmp)
    return calc(arr, 3, 1)

# part2 : calculate number of trees encountered when taking 5 different paths,
#	  return their product
def part2():
    arr = []
    with open("Day 3 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    count = 0
    for i in range(len(lines)):
        un = lines[i]
        if un[-1] == '\n':
            un = un[:-1]
        tmp = []
        for i in range(len(un)):
            tmp.append(un[i])
        arr.append(tmp)
    s1 = calc(arr, 1, 1)
    s2 = calc(arr, 3, 1)
    s3 = calc(arr, 5, 1)
    s4 = calc(arr, 7, 1)
    s5 = calc(arr, 1, 2)
    return s1 * s2 * s3 * s4 * s5
