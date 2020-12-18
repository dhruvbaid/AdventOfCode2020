# process1 : evaluate expression left-to-right, parentheses > *,+ priority
def process1(line):
    # remove spaces from input
    line = line.replace(" ","")

    # recursively process based on whether there are parentheses or not
    if "(" not in line:
        if(("+" not in line) and ("*" not in line)):
            return int(line)
        else:
            i = 0
            while line[i] not in ["+","*"]:
                i += 1
            res = int(line[:i])
            while i < len(line):
                if line[i] == "*":
                    j = i+1
                    while line[j] not in ["*", "+"]:
                        if j == len(line) - 1:
                            j = len(line)
                            break
                        else:
                            j += 1
                    res *= int(line[i+1:j])
                    i = j
                elif line[i] == "+":
                    j = i+1
                    while line[j] not in ["*", "+"]:
                        if j == len(line) - 1:
                            j = len(line)
                            break
                        else:
                            j += 1
                    res += int(line[i+1:j])
                    i = j
                else:
                    print("Error")
                    i += 2
            return res
    else:
        f = 0
        while line[f] != "(":
            f += 1
        count = 1
        l = f+1
        while count > 0:
            if line[l] == "(":
                count += 1
            if line[l] == ")":
                count -= 1
            l += 1
        tmpRes = process1(line[f+1 : l-1])
        newLine = line[ : f] + str(process1(line[f+1 : l-1])) + line[l : ]
        return process1(newLine)

# part1 : uses process1 to process each line, returns sum of outputs
def part1():
    with open("Day 18 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    res = 0
    
    for i in range(len(lines)):
        res += process1(lines[i])

    print(res)
    return

# process2 : evaluate expression left-to-right, parentheses > + > * priority
def process2(line):
    # remove spaces from input
    line = line.replace(" ","")

    # recursively process based on whether there are parentheses or not
    if "(" not in line:
        if(("+" not in line) and ("*" not in line)):
            return int(line)
        else:
            a = line.split("*")
            # print(a)
            for i in range(len(a)):
                a[i] = process1(a[i])
            res = 1
            for i in range(len(a)):
                res *= int(a[i])
            return res
    else:
        f = 0
        while line[f] != "(":
            f += 1
        count = 1
        l = f+1
        while count > 0:
            if line[l] == "(":
                count += 1
            if line[l] == ")":
                count -= 1
            l += 1
        tmpRes = process2(line[f+1 : l-1])
        newLine = line[ : f] + str(process2(line[f+1 : l-1])) + line[l : ]
        return process2(newLine)

# part2 : uses process2 to process each line, returns sum of outputs
def part2():
    with open("Day 18 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    res = 0
    
    for i in range(len(lines)):
        res += process2(lines[i])

    print(res)
    return

# main : runs parts 1 and 2
def main():
    part1()
    part2()
    return
