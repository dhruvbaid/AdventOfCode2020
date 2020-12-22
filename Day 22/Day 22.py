# part1 : Given 2 hands, play a normal game where each player deals their top
#         card, and the higher card wins. Winner takes both cards and puts it
#         at the bottom of their deck (higher value on top), game continues till
#         one player runs out of cards (other one wins). Calculate weighted
#         score.
def part1():
    with open("Day 22 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # get players' hands
    p1 = []
    p2 = []
    
    i = 1
    while lines[i] != "":
        p1.append(int(lines[i]))
        i += 1
    i += 2
    while i < len(lines):
        p2.append(int(lines[i]))
        i += 1

    # play the game
    while((len(p1) > 0) and (len(p2) > 0)):
        p1Cur = p1[0]
        p2Cur = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        if p1Cur > p2Cur:
            p1 += [p1Cur, p2Cur]
        else:
            p2 += [p2Cur, p1Cur]

    # calculate winner's score
    res = 0
    if len(p1) == 0:
        for i in range(len(p2)):
            res += (len(p2) - i)*p2[i]
    else:
        for i in range(len(p1)):
            res += (len(p1) - i)*p1[i]
    
    print(f"Part 1: {res}")
    return

# playRecursive : given two hands, play the recursive game (this function will
#                 obviously be called recursively)
def playRecursive(p1: list, p2: list):
    gameRounds = []
    while((len(p1) > 0) and (len(p2) > 0)):
        if [p1, p2] in gameRounds:
            return ["p1", p1]

        gameRounds.append([p1,p2])
        
        p1Cur = p1[0]
        p2Cur = p2[0]

        p1 = p1[1:]
        p2 = p2[1:]

        if((len(p1) >= p1Cur) and (len(p2) >= p2Cur)):
            # new game
            p1New = []
            for i in range(p1Cur):
                p1New.append(p1[i])
            p2New = []
            for i in range(p2Cur):
                p2New.append(p2[i])
            winner = playRecursive(p1New, p2New)
            if winner[0] == "p1":
                p1 += [p1Cur, p2Cur]
            else:
                p2 += [p2Cur, p1Cur]
        else:
            if p1Cur > p2Cur:
                p1 += [p1Cur, p2Cur]
            else:
                p2 += [p2Cur, p1Cur]

    if len(p1) == 0:
        return ["p2", p2]
    else:
        return ["p1", p1]

# part2 : make both players play the recursive game, and return the winner's
#         weighted score.
def part2():
    with open("Day 22 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # get players' hands
    p1 = []
    p2 = []
    
    i = 1
    while lines[i] != "":
        p1.append(int(lines[i]))
        i += 1
    i += 2
    while i < len(lines):
        p2.append(int(lines[i]))
        i += 1

    # play the game
    win = playRecursive(p1, p2)

    # calculate winner's score
    res = 0
    for i in range(len(win[1])):
        res += (len(win[1]) - i)*win[1][i]

    print(f"Part 2: {res}")
    return

# main : runs part1() and part2()
def main():
    part1()
    part2()
