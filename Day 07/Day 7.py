# part1 : Get list of bags which eventually contain a shiny golden bag
def part1():
    with open("Day 7 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # separate container from containees
    for i in range(len(lines)):
        lines[i] = lines[i].split(" bags contain ")

    bagRules = []

    # rule processing
    for i in range(len(lines)):
        if("," in lines[i][1]):
            # multiple bags
            tmp = lines[i][1].split(", ")
            cols = []
            for j in range(len(tmp)):
                cur_rule = tmp[j].split(" ")
                col = cur_rule[1] + " " + cur_rule[2]
                cols.append(col)
            bagRules.append((lines[i][0], cols))
        elif lines[i][1] == "no other bags.":
            # contains no others
            bagRules.append((lines[i][0], [])) 
        else:
            # one other bad
            tmp = lines[i][1].split(" ")
            col = tmp[1] + " " + tmp[2]
            bagRules.append((lines[i][0], [col]))

    # create a set which contains all colors which may eventually contain
    # shiny golden
    c = set()

    # initial round: all bags which directly contain shiny golden
    for i in range(len(bagRules)):
        if "shiny gold" in bagRules[i][1]:
            c.add(bagRules[i][0])

    # subsequently, all bags which contain bags which... contain shiny golden
    count = 1
    while(count > 0):
        count = 0
        tmp = []
        for x in c:
            for i in range(len(bagRules)):
                if x in bagRules[i][1]:
                    if bagRules[i][0] not in c:
                        tmp.append(bagRules[i][0])
                        count += 1
        for b in tmp:
            c.add(b)

    # result: all bags which eventually contain shiny golden
    return len(c)

# count : given a list of rules (processed), find the number of bags in a
#         input bag color by recursively looking through all the bags this bag
#         contains.
# Assumption: termination (0 bags) ALWAYS happens.
# Validity  : TRUE because of physical constraints (no containment loops)
def count(bagCol, bagRules):
    res = 0
    for i in range(len(bagRules)):
        if bagRules[i][0] == bagCol:
            # correct bag - look through each bag inside
            for bag in bagRules[i][1]:
                res += 1
                res += count(bag, bagRules)
    return res

# part2 : processes rules differently to get right input for count
def part2():
    with open("Day 7 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # separate container from containees
    for i in range(len(lines)):
        lines[i] = lines[i].split(" bags contain ")

    bagRules = []

    # rule processing
    for i in range(len(lines)):
        if("," in lines[i][1]):
            # multiple bags
            tmp = lines[i][1].split(", ")
            cols = []
            for j in range(len(tmp)):
                cur_rule = tmp[j].split(" ")
                col = cur_rule[1] + " " + cur_rule[2]
                for times in range(int(cur_rule[0])):
                    cols.append(col)
            bagRules.append((lines[i][0], cols))
        elif lines[i][1] == "no other bags.":
            # contains no others
            bagRules.append((lines[i][0], [])) 
        else:
            # one other bad
            tmp = lines[i][1].split(" ")
            col = tmp[1] + " " + tmp[2]
            for times in range(int(tmp[0])):
                bagRules.append((lines[i][0], [col]))

    return count("shiny gold", bagRules)

# main : prints part1() and part2() results
def main():
    print(part1())
    print(part2())
    return
