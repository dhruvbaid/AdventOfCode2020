# part1 : Get sum of cardinality of union of sets formed by input
def part1():
    with open("Day 6 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    counts = []
    questions = set()
    for i in range(len(lines)):
        if(i == len(lines) - 1):
            if(lines[i] == ''):
                counts.append(len(questions))
                questions = set()
            else:
                for letter in lines[i]:
                    questions.add(letter)
                counts.append(len(questions))
        else:
            if(lines[i] == ''):
                counts.append(len(questions))
                questions = set()
            else:
                for letter in lines[i]:
                    questions.add(letter)
    
    print(f"Part 1: {sum(counts)}")

# part1 : Get sum of cardinality of intersection of sets formed by input
def part2():
    with open("Day 6 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    resp = []
    tmp = []
    for i in range(len(lines)):
        if i == len(lines) - 1:
            if lines[i] == '':
                resp.append(tmp)
                tmp = []
            else:
                tmp.append(lines[i])
                resp.append(tmp)
        else:
            if lines[i] == '':
                resp.append(tmp)
                tmp = []
            else:
                tmp.append(lines[i])

    counts = []
    for j in range(len(resp)):
        curr = resp[j]
        questions = []
        for k in range(len(curr)):
            if k == 0:
                for letter in curr[k]:
                    questions.append(letter)
            else:
                tmp = []
                for letter in curr[k]:
                    if letter in questions:
                        tmp.append(letter)
                questions = tmp
        counts.append(len(questions))

    print(f"Part 2: {sum(counts)}")

# main : run both parts
def main():
    part1()
    part2()
