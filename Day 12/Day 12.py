# part1 : get final position of ship based on absolute changes
def part1():
    with open("Day 12 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]
        lines[i] = [lines[i][0], int(lines[i][1:])]

    facing = ["E", "N", "W", "S"]
    cur_face = 0
    cur_pos = [0,0]
    for i in range(len(lines)):
        cur_ins = lines[i][0]
        cur_val = lines[i][1]

        if cur_ins == "N":
            cur_pos[1] += cur_val
        elif cur_ins == "S":
            cur_pos[1] -= cur_val
        elif cur_ins == "E":
            cur_pos[0] += cur_val
        elif cur_ins == "W":
            cur_pos[0] -= cur_val
        elif cur_ins == "L":
            num = cur_val/90
            cur_face += num
            cur_face = cur_face%4
        elif cur_ins == "R":
            num = cur_val/90
            cur_face -= num
            while cur_face < 0:
                cur_face += 4
        elif cur_ins == "F":
            if cur_face == 0:
                cur_pos[0] += cur_val
            elif cur_face == 1:
                cur_pos[1] += cur_val
            elif cur_face == 2:
                cur_pos[0] -= cur_val
            elif cur_face == 3:
                cur_pos[1] -= cur_val
            else:
                print("Error")
        else:
            print("Error")
    print(abs(cur_pos[0]) + abs(cur_pos[1]))
    return

# part1 : get final position of ship based on waypoint coordinates
def part2():
    with open("Day 12 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]
        lines[i] = [lines[i][0], int(lines[i][1:])]

    wp = [10,1]
    facing = ["E", "N", "W", "S"]
    cur_face = 0
    cur_pos = [0,0]
    for i in range(len(lines)):
        cur_ins = lines[i][0]
        cur_val = lines[i][1]

        if cur_ins == "N":
            wp[1] += cur_val
        elif cur_ins == "S":
            wp[1] -= cur_val
        elif cur_ins == "E":
            wp[0] += cur_val
        elif cur_ins == "W":
            wp[0] -= cur_val
        elif cur_ins == "L":
            num = int(cur_val/90)
            for i in range(num):
                x = wp[0]
                y = wp[1]
                wp = [-y, x]
        elif cur_ins == "R":
            num = int(cur_val/90)
            for i in range(num):
                x = wp[0]
                y = wp[1]
                wp = [y, -x]
        elif cur_ins == "F":
            for i in range(cur_val):
                cur_pos[0] += wp[0]
                cur_pos[1] += wp[1]
        else:
            print("Error")
    print(abs(cur_pos[0]) + abs(cur_pos[1]))
    return
