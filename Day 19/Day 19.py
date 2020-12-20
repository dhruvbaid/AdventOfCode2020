"""
SOLUTIONS NOT MY OWN
SOURCE: https://github.com/borjasotomayor/AoC/blob/main/2020/day19.py
"""

import lark

# aoc2lark : Converts the given grammar to a Lark grammar
def aoc2lark(rules):
    grammar = ""
    for line in rules:
        ruleNum, subrules = line.split(": ")
        ruleNum = int(ruleNum)
        if ruleNum == 0:
            ruleName = "start"
        else:
            ruleName = f"rule{ruleNum}"

        if "|" in subrules:
            subrule1, subrule2 = subrules.split(" | ")

            subrule1 = " ".join("rule" + x for x in subrule1.split())
            subrule2 = " ".join("rule" + x for x in subrule2.split())

            subrules_new = f"{subrule1} | {subrule2}"

        elif subrules[0] == '"':
            subrules_new = subrules
        else:
            subrules_new = " ".join("rule" + x for x in subrules.split())

        grammar += f"{ruleName}: {subrules_new}\n"

    return grammar

# part1 : parses given input and returns number of correct messages
def part1():
    with open("Day 19 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # split input into rules and messages
    allRules = []
    messages = []
    for i in range(len(lines)):
        if lines[i] == "":
            break
        allRules.append(lines[i])

    i += 1
    
    while i < len(lines):
        messages.append(lines[i])
        i += 1

    # convert to grammar
    grammar = aoc2lark(allRules)

    # obtain correct number of messages
    correct = 0
    parser = lark.Lark(grammar)
    for message in messages:
        try:
            parser.parse(message.strip())
            correct += 1
        except lark.exceptions.LarkError:
            pass

    return correct

# part2 : edits input rules and returns number of correct messages
def part2():
    with open("Day 19 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # split input into rules and messages
    allRules = []
    messages = []
    for i in range(len(lines)):
        if lines[i] == "":
            break
        allRules.append(lines[i])

    i += 1
    
    while i < len(lines):
        messages.append(lines[i])
        i += 1

    # replace old rules with new ones
    newRules = []
    for line in allRules:
        if line == "8: 42":
            line = "8: 42 | 42 8"
        elif line == "11: 42 31":
            line = "11: 42 31 | 42 11 31"
        newRules.append(line)

    # convert to grammar
    grammar = aoc2lark(newRules)

    # obtain correct number of messages
    correct = 0
    parser = lark.Lark(grammar)
    for message in messages:
        try:
            parser.parse(message.strip())
            correct += 1
        except lark.exceptions.LarkError:
            pass

    return correct

# main : runs part1 and part2
def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
