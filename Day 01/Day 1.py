def part1():
    arr = []
    with open("Day 1 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    print(len(lines))
    for x in lines:
        arr.append(int(x))
    for i in range(len(arr)):
        n1 = arr[i]
        n2 = 2020 - n1
        if n2 in arr:
            return n1 * n2

def part2():
    arr = []
    with open("Day 1 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    print(len(lines))
    for x in lines:
        arr.append(int(x))
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            n1 = arr[i]
            n2 = arr[j]
            n3 = 2020 - n1 - n2
            if n3 in arr:
                return n1 * n2 * n3
