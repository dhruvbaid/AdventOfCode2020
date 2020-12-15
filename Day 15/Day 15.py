# main : runs code for parts 1 (n = 2020) and 2 (n = 300000000) - stores order
#        of calling out numbers as the values in a key-value pair in a dict,
#        and uses that to determine what the next value will be (previously
#        called value is stored as a separate prev variable)
def main(n: int):
    with open("Day 15 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]
    for i in range(len(lines)):
        lines[i] = lines[i].split(",")
    lines = lines[0]

    d = dict()
    numbers = []
    for i in range(1, n + 1):
        if i <= len(lines):
            if int(lines[i-1]) in d:
                d[int(lines[i-1])].append(i)
            else:
                d[int(lines[i-1])] = [i]
            prev = lines[i-1]
        else:
            if prev in d:
                if len(d[prev]) == 1:
                    if 0 in d:
                        d[0].append(i)
                    else:
                        d[0] = [i]
                    prev = 0
                else:
                    diff = d[prev][-1] - d[prev][-2]
                    if diff in d:
                        d[diff].append(i)
                    else:
                        d[diff] = [i]
                    prev = diff
            else:
                if 0 in d:
                    d[0].append(i)
                else:
                    d[0] = [i]
                prev = 0

    print(prev)
    return
