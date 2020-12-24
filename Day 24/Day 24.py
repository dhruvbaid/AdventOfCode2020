# neighbors : given a tile, return a list of its neighbors
def neighbors(tile):
    tileX = tile[0]
    tileY = tile[1]
    return [(tileX - 1, tileY),
            (tileX - 0.5, tileY + 1),
            (tileX + 0.5, tileY + 1),
            (tileX + 1, tileY),
            (tileX + 0.5, tileY - 1),
            (tileX - 0.5, tileY - 1)]

# main : do parts 1 and 2
def main():
    with open("Day 24 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # black contains all black tiles
    black = []

    # part 1: follow the instructions and flip the correct tiles
    for i in range(len(lines)):
        cur = [0,0]
        j = 0
        while j < len(lines[i]):
            move = lines[i][j]
            if move == "e":
                cur[0] += 1
                j += 1
            elif move == "w":
                cur[0] -= 1
                j += 1
            elif move == "n":
                j += 1
                if lines[i][j] == "e":
                    cur[0] += 0.5
                    cur[1] += 1
                    j += 1
                else:
                    cur[0] -= 0.5
                    cur[1] += 1
                    j += 1
            elif move == "s":
                j += 1
                if lines[i][j] == "e":
                    cur[0] += 0.5
                    cur[1] -= 1
                    j += 1
                else:
                    cur[0] -= 0.5
                    cur[1] -= 1
                    j += 1
        if cur in black:
            # flip black to white
            black.remove(cur)
        else:
            # flip white to black
            black.append(cur)
    print(f"Part 1: {len(black)}")

    # d contains ALL tiles which might be affected in 100 days' time
    d = dict()
    x = -105
    while x < 105:
        y = -105
        while y < 105:
            if [x,y] in black:
                d[(x,y)] = 1
            else:
                d[(x,y)] = 0
            y += 0.5
        x += 0.5

    # part 2: do the flips for each day
    for day in range(100):
        b2w = []
        w2b = []

        for tile in d:
            if d[tile] == 1:
                # black tile
                n = neighbors(tile)
                bN = 0
                for t in n:
                    if t in d:
                        if d[t] == 1:
                            bN += 1
                            if bN > 2:
                                break
                if bN == 0 or bN > 2:
                    b2w.append(tile)
            else:
                # white tile
                n = neighbors(tile)
                bN = 0
                for t in n:
                    if t in d:
                        if d[t] == 1:
                            bN += 1
                            if bN > 2:
                                break
                if bN == 2:
                    w2b.append(tile)

        for t in b2w:
            d[t] = 0
        for t in w2b:
            d[t] = 1

    count = 0
    for x in d:
        if d[x] == 1:
            count += 1
    print(f"Part 2: {count}")
    return
