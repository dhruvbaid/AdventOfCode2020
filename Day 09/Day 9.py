# main : checks through list of integers to see which is NOT a sum of 2 distinct
#        integers among the previous 25, and then find a contiguous list which
#        does sum to this 'incorrect' number and return the sum of the min and
#        max of this contiguous list
def main():
    with open("Day 9 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = int(lines[i].split("\n")[0])

    # check if current number is a sum of 2 distinct numbers in previous 25
    for i in range(25, len(lines)):
        prev = lines[i - 25:i]
        valid = 0
        for j in range(len(prev)):
            for k in range(j + 1, len(prev)):
                if prev[j] + prev[k] == lines[i]:
                    valid = 1
                    i += 1
                    break
            if valid == 1:
                break
        if valid == 0:
            wrong = lines[i]
            print(f"Part 1: {wrong}")

    # get list of all numbers up to the 'wrong' one
    prev = lines[:i]

    # sum contiguously and try to create the 'wrong' number
    for j in range(len(prev)):
        exceed = 0
        for k in range(j+1, len(prev)):
            if sum(prev[j:k+1]) == wrong:
                print(f"Part 2: {min(prev[j:k+1]) + max(prev[j:k+1])}")
            elif sum(prev[j:k+1]) > wrong:
                exceed = 1
                break
    return
