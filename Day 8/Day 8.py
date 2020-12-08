# main : process list of instructions and call either executeNoChange() for Part
#        1 or executeWithChange() for Part 2
def main():
    with open("Day 8 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    instructions = []
    for i in range(len(lines)):
        instructions.append((lines[i][0:3], lines[i][4:]))

    print(f"Part 1: {executeNoChange(instructions)}")
    b = executeWithChange(instructions)

# executeNoChange : do not change instructions, simply return acc value before
#                   first repeat instruction, or "YES" if instruction has
#                   reached the line after last line of real instructions (i.e.
#                   successful run)
def executeNoChange(instructions):
    sequence = []
    i = 0
    acc = 0
    while(True):
        if i in sequence:
            # repeat instruction, return accumulator value
            return acc
        if i == len(instructions):
            # successful run
            print(f"Part 2: {acc}")
            return "YES"
        if i > len(instructions):
            # messed up, just exit
            return

        # append instruction number to sequence of instructions
        sequence.append(i)

        # store and process current instruction
        curr = instructions[i]
        if curr[0] == "nop":
            i += 1
        elif curr[0] == "acc":
            val = curr[1]
            if val[0] == "+":
                acc += int(val[1:])
            else:
                acc -= int(val[1:])
            i += 1
        else:
            val = curr[1]
            if val[0] == "+":
                i += int(val[1:])
            else:
                i -= int(val[1:])

# executeWithChange : whenever a nop or jmp is encountereed, change it to a jmp
#                     or nop respectively, and try to run the new instructions.
#                     If successful, return accumulator value; otherwise, ignore
#                     that run and continue normal processing.
def executeWithChange(instructions):
    sequence = []
    i = 0
    acc = 0
    while(True):
        if i in sequence:
            # repeated instruction, return accumulator value
            return acc
        if i == len(instructions) - 1:
            print(f"acc = {acc}")
            return "YES"
        sequence.append(i)
        curr = instructions[i]
        if curr[0] == "nop":
            # try changing nop to jmp
            tmp = []
            for x in instructions:
                tmp.append(x)
            tmp[i] = ("jmp", tmp[i][1])
            if executeNoChange(tmp) == "YES":
                # print(f"acc real = {acc}")
                return
            else:
                # changed instruction was unsuccessful, continue
                i += 1
        elif curr[0] == "acc":
            val = curr[1]
            if val[0] == "+":
                acc += int(val[1:])
            else:
                acc -= int(val[1:])
            i += 1
        else:
            # try changing jmp to nop
            tmp = []
            for x in instructions:
                tmp.append(x)
            tmp[i] = ("nop", tmp[i][1])
            if executeNoChange(tmp) == "YES":
                # print(f"acc real = {acc}")
                return
            else:
                # changed instruction was unsuccessful, continue
                val = curr[1]
                if val[0] == "+":
                    i += int(val[1:])
                else:
                    i -= int(val[1:])
