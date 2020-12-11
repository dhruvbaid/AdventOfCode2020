def part1():
    arr = []
    with open("Day 2 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    count = 0
    for x in lines:
        a1 = x.split(" ")
        bounds = a1[0].split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])
        letter = a1[1][:-1]
        password = a1[2]
        if lower <= password.count(letter) <= upper:
            count += 1
    return count

def part2():
    arr = []
    with open("Day 2 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    count = 0
    for x in lines:
        a1 = x.split(" ")
        bounds = a1[0].split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])
        letter = a1[1][:-1]
        password = a1[2]
        if (password[lower - 1] == letter) or (password[upper - 1] == letter):
            if(not((password[lower - 1] == letter) and (password[upper - 1] == letter))):
                count += 1
    return count
