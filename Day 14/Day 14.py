# toBinary : converts an input (string) in decimal to a 36-bit binary number
def toBinary(dec: str):
    res = ""
    intDec = int(dec)
    for i in range(36):
        if 2**(35 - i) <= intDec:
            res += "1"
            intDec -= 2**(35 - i)
        else:
            res += "0"
    return res

# noX : given an input string (basically a binary sequence with X's), return an
#       array which converts EACH X into a 0 or 1 (i.e. length = 2^(no. of X's))
def noX(binLocation: str):
    res = ""
    vals = []
    for i in range(len(binLocation)):
        if binLocation[i] == "X":
            res1 = res
            res2 = res
            res1 += "0" + binLocation[i+1:]
            res2 += "1" + binLocation[i+1:]
            vals1 = noX(res1)
            vals2 = noX(res2)
            vals += vals1
            vals += vals2
            return vals
        else:
            res += binLocation[i]
    return [res]

# toInt : converts a binary string into a decimal number
def toInt(binary : str):
    res = 0
    for i in range(len(binary)):
        res += int(binary[i]) * (2**(len(binary) - 1 - i))
    return res

# part1 : update address with mask&value, with some conditions on the mask
#         containing X's; return sum of values at all addresses
def part1():
    with open("Day 14 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    res = 0
    d = dict()
    
    for i in range(len(lines)):
        if lines[i][0:4] == "mask":
            mask = lines[i].split("=")[1][1:]
        else:
            start = 0
            end = 0
            readLine = lines[i].split(" = ")

            # get address
            location = readLine[0]
            for i in range(len(location)):
                if location[i] == "[":
                    start = i+1
                if location[i] == "]":
                    end = i

            # convert address to integer
            location = int(location[start:end])

            # get value to be written to address
            value = toBinary(readLine[1])

            # perform value&mask check
            finalValue = ""
            for i in range(len(value)):
                if mask[i] == "X":
                    finalValue += str(value[i])
                else:
                    finalValue += str(mask[i])

            # write value to memory location
            d[location] = finalValue

    # sum values in all memory addresses
    for x in d:
        val = d[x]
        res += toInt(val)

    print(res)
    return

# part2 : writes value to address&mask (but each X in mask generates 2 addresses
#         where X is replaced with 0 or 1). Return sum of vals at all addresses
def part2():
    with open("Day 14 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    res = 0
    d = dict()
    
    for i in range(len(lines)):
        if lines[i][0:4] == "mask":
            mask = lines[i].split("=")[1][1:]
        else:
            start = 0
            end = 0
            readLine = lines[i].split(" = ")

            # get address
            location = readLine[0]
            for i in range(len(location)):
                if location[i] == "[":
                    start = i+1
                if location[i] == "]":
                    end = i
            location = int(location[start:end])

            # convert decimal address to binary
            binLocation = toBinary(str(location))

            # get value to be written to address
            value = int(readLine[1])

            # perform mask&address check
            finalLocation = ""
            for i in range(len(binLocation)):
                if mask[i] == "X":
                    finalLocation += "X"
                elif mask[i] == "1":
                    finalLocation += "1"
                elif mask[i] == "0":
                    finalLocation += binLocation[i]
                else:
                    print("ERROR")

            # process X's in address
            addresses = noX(finalLocation)

            # write value to memory locations
            for address in addresses:
                d[toInt(address)] = value

    # sum values in all memory addresses
    for x in d:
        res += d[x]

    print(res)
    return
