# part1 : look at all adjacent seats, check number of empty/full, change until
#         stable solution is reached, return number of occupied seats
def part1():
    with open("Day 11 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = list(lines[i].split("\n")[0])

    newArr = []
    for i in range(len(lines)):
        tmp = []
        for j in range(len(lines[i])):
            tmp.append(lines[i][j])
        newArr.append(tmp)

    while(True):        
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                curr = lines[row][col]
                adj = []
                # get indices of all adjacent seats
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        # check validity of x and y
                        if((x >= 0) and
                           (y >= 0) and
                           (x <= len(lines) - 1) and
                           (y <= len(lines[0]) - 1)):
                            adj.append((x,y))
                # seat is not adjacent to itself
                adj.remove((row, col))

                # convert indices to actual seat values (#, ., L)
                for i in range(len(adj)):
                    adj[i] = lines[adj[i][0]][adj[i][1]]

                # get number of occupied adjacent seats
                occupied = adj.count("#")

                # change seats which need to be changed (in newArr)
                if((curr == "L") and (occupied == 0)):
                    newArr[row][col] = "#"
                elif((curr == "#") and (occupied >= 4)):
                    newArr[row][col] = "L"
                else:
                    continue

        if lines == newArr:
            break
        else:
            lines = []
            for i in range(len(newArr)):
                tmp = []
                for j in range(len(newArr[i])):
                    tmp.append(newArr[i][j])
                lines.append(tmp)

    # get final count of occupied seats
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                count += 1

    print(count)
    return

# part2 : instead of looking at all adjacent seats, look at the seats in all
#         directions which can be seen (i.e. separated by floor only), do the
#         same thing as part1 (different value for changing unoccupied to
#         occupied, though)
def part2():
    with open("Day 11 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = list(lines[i].split("\n")[0])

    newArr = []
    for i in range(len(lines)):
        tmp = []
        for j in range(len(lines[i])):
            tmp.append(lines[i][j])
        newArr.append(tmp)

    while(True):
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                curr = lines[row][col]
                vis = []

                # look in all 8 directions (manually), get visible seats
                # left
                x = col - 1
                while x >= 0 and lines[row][x] == ".":
                    x -= 1
                if x != -1:
                    vis.append(lines[row][x])

                # right
                x = col + 1
                while x < len(lines[0]) and lines[row][x] == ".":
                    x += 1
                if x != len(lines[0]):
                    vis.append(lines[row][x])

                # up
                y = row - 1
                while y >= 0 and lines[y][col] == ".":
                    y -= 1
                if y != -1:
                    vis.append(lines[y][col])

                # down
                y = row + 1
                while y < len(lines) and lines[y][col] == ".":
                    y += 1
                if y != len(lines):
                    vis.append(lines[y][col])

                # upleft
                x = col - 1
                y = row - 1
                while((x >= 0) and
                      (y >= 0) and
                      (lines[y][x] == ".")):
                    x -= 1
                    y -= 1
                if((x != -1) and (y != -1)):
                    vis.append(lines[y][x])

                # upright
                x = col + 1
                y = row - 1
                while((x < len(lines[0])) and
                      (y >= 0) and
                      (lines[y][x] == ".")):
                    x += 1
                    y -= 1
                if((x != len(lines[0])) and (y != -1)):
                    vis.append(lines[y][x])

                # downleft
                x = col - 1
                y = row + 1
                while((x >= 0) and
                      (y < len(lines)) and
                      (lines[y][x] == ".")):
                    x -= 1
                    y += 1
                if((x != -1) and (y != len(lines))):
                   vis.append(lines[y][x])

                # downright
                x = col + 1
                y = row + 1
                while((x < len(lines[0])) and
                      (y < len(lines)) and
                      (lines[y][x] == ".")):
                    x += 1
                    y += 1
                if((x != len(lines[0])) and (y != len(lines))):
                    vis.append(lines[y][x])

                # get number of occupied adjacent seats
                occupied = vis.count("#")

                # change seats which need to be changed (in newArr)
                if((curr == "L") and (occupied == 0)):
                    newArr[row][col] = "#"
                elif((curr == "#") and (occupied >= 5)):
                    newArr[row][col] = "L"
                else:
                    continue

        if lines == newArr:
            break
        else:
            lines = []
            for i in range(len(newArr)):
                tmp = []
                for j in range(len(newArr[i])):
                    tmp.append(newArr[i][j])
                lines.append(tmp)

    # get final count of occupied seats
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                count += 1

    print(count)
    return
