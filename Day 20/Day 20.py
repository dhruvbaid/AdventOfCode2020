# convert : converts a string of #s and .s to a binary number (# = 1, . = 0)
def convert(a: str):
    res1 = 0
    for i in range(len(a)):
        if a[i] == "#":
            res1 = res1 | (1 << i)
    b = a[::-1]
    res2 = 0
    for i in range(len(b)):
        if b[i] == "#":
            res2 = res2 | (1 << i)
    return [res1, res2]

# part1 : converts the borders of tiles to binary numbers, checks frequency of
#         each to see which ones come from corner tiles
def part1():
    with open("Day 20 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    tiles = []
    tmp = []
    for i in range(len(lines)):
        if lines[i] == "":
            tiles.append(tmp)
            tmp = []
        else:
            tmp.append(lines[i])
    tiles.append(tmp)
    
    d = dict()
    fullTiles = dict()
    
    for i in range(len(tiles)):
        tileNum = int(tiles[i][0][5:-1])
        tile = tiles[i][1:]
        fullTiles[tileNum] = tile
        top = tile[0]
        bottom = tile[-1]
        left = ""
        right = ""
        for i in range(len(tile)):
            left += tile[i][0]
            right += tile[i][-1]
        d[tileNum] = [convert(top),
                      convert(right),
                      convert(bottom),
                      convert(left)]

    tb = []
    lr = []
    for tNum in d:
        tb += d[tNum][0]
        tb += d[tNum][2]
        lr += d[tNum][1]
        lr += d[tNum][3]

    tbD = dict()
    for x in set(tb):
        tbD[x] = tb.count(x)
    lrD = dict()
    for y in set(lr):
        lrD[y] = lr.count(y)

    a = tb+lr
    aD = dict()
    for z in set(a):
        aD[z] = a.count(z)

    score = dict()
    for tNum in d:
        s = 0
        for i in range(4):
            side = d[tNum][i]
            for rot in side:
                if aD[rot] == 2:
                    s += 1
                    break
        score[tNum] = s

    corners = []
    res = 1
    for tNum in score:
        if score[tNum] == 2:
            corners.append(tNum)
            res *= tNum

    print(f"Part 1: {res}")
    return

"""
-------------------------------------------------------------------------------
PART 2 SOLUTION NOT MY OWN.
SOURCE: https://github.com/morgoth1145/advent-of-code/blob/2020-python/2020/
        Day%2020/solution.py
-------------------------------------------------------------------------------
"""
import collections
import math
import re

def parse_tiles(s):
    tiles = {}
    for part in s.split('\n\n'):
        lines = part.splitlines()
        m = re.fullmatch('Tile (\d+):', lines[0])
        num = int(m.group(1))
        grid = [list(l) for l in lines[1:]]
        tiles[num] = grid
    return tiles

def determine_grid_borders(grid):
    top = grid[0]
    right = ''.join(l[-1] for l in grid)
    bottom = grid[-1]
    left = ''.join(l[0] for l in grid)
    return (top, right, bottom, left)

def grid_mirrors(grid):
    candidates = [grid]
    candidates.append(grid[::-1])
    candidates.append([l[::-1] for l in grid])
    candidates.append([l[::-1] for l in grid][::-1])
    return candidates

def grid_rotations(grid):
    candidates = [grid]
    last = grid
    for _ in range(3):
        grid = [l[:] for l in grid]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid[x][y] = last[len(grid[x])-y-1][x]
        last = grid
        candidates.append(grid)
    return candidates

def all_grid_options(grid):
    candidates = list()
    for opt in grid_mirrors(grid):
        candidates.extend(grid_rotations(opt))
    output = []
    for opt in candidates:
        if opt not in output:
            output.append(opt)
    return output

def generate_tiling(tile_to_orients_to_borders):
    dim = math.isqrt(len(tile_to_orients_to_borders))
    def impl(tiling, x, y, seen):
        if y == dim:
            return tiling
        next_x = x+1
        next_y = y
        if next_x == dim:
            next_x = 0
            next_y += 1
        for num, options in tile_to_orients_to_borders.items():
            if num in seen:
                continue
            seen.add(num)
            for idx, borders in options.items():
                top, _, _, left = borders
                if x > 0:
                    neighbor_num, neighbor_orient = tiling[x-1][y]
                    _, neighbor_right, _, _ = tile_to_orients_to_borders[neighbor_num][neighbor_orient]
                    if neighbor_right != left:
                        continue
                if y > 0:
                    neighbor_num, neighbor_orient = tiling[x][y-1]
                    _, _, neighbor_bottom, _ = tile_to_orients_to_borders[neighbor_num][neighbor_orient]
                    if neighbor_bottom != top:
                        continue
                tiling[x][y] = (num, idx)
                answer = impl(tiling, next_x, next_y, seen)
                if answer is not None:
                    return answer
            seen.remove(num)
        tiling[x][y] = None
        return None
    tiling = [[None] * dim for _ in range(dim)]
    return impl(tiling, 0, 0, set())

def make_superimage(tile_options, tiling):
    output = []
    for row in tiling:
        grids = []
        for num, orient in row:
            grid = tile_options[num][orient]
            # Chop off borders
            grid = [l[1:-1] for l in grid[1:-1]]
            grids.append(grid)
        for y in range(len(grids[0][0])):
            out_row = []
            for idx in range(len(grids)):
                out_row.extend(grids[idx][x][y] for x in range(len(grids[idx])))
            output.append(''.join(out_row))
    return output

MONSTER_PATTERN = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

def test_for_monsters(image):
    monster_coords = []
    max_x = 0
    max_y = 0
    for dy, line in enumerate(MONSTER_PATTERN.splitlines()):
        for dx, c in enumerate(line):
            if c == '#':
                monster_coords.append((dx, dy))
                max_x = max(dx, max_x)
                max_y = max(dy, max_y)
    monster_tiles = set()
    for y in range(len(image)):
        if y+max_y >= len(image):
            break
        for x in range(len(image[y])):
            if x+max_x >= len(image[y]):
                break
            has_monster = True
            for dx, dy in monster_coords:
                if image[y+dy][x+dx] != '#':
                    has_monster = False
                    break
            if has_monster:
                for dx, dy in monster_coords:
                    monster_tiles.add((x+dx, y+dy))
    if len(monster_tiles) == 0:
        return None
    all_pounds = set()
    for y, row in enumerate(image):
        for x, c in enumerate(row):
            if c == '#':
                all_pounds.add((x, y))
    return len(all_pounds - monster_tiles)

def part2(s):
    tiles = parse_tiles(s)
    tile_options = {num:all_grid_options(grid)
                    for num, grid in tiles.items()}
    tile_to_orients_to_borders = collections.defaultdict(dict)
    for num, options in tile_options.items():
        for idx, grid in enumerate(options):
            borders = determine_grid_borders(grid)
            tile_to_orients_to_borders[num][idx] = borders
    tiling = generate_tiling(tile_to_orients_to_borders)

    image = make_superimage(tile_options, tiling)

    image_opts = all_grid_options([list(l) for l in image])

    for opt in image_opts:
        answer = test_for_monsters(opt)
        if answer is not None:
            break
    
    print(f"Part 2: {answer}")

part1()
part2(open('Day 20 Input.txt').read().strip())
