# part1 : obtain encryption key from cardLoop/doorLoop
def main():
    with open("Day 25 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    cardVal = int(lines[0])
    doorVal = int(lines[1])
    
    cardLoop = 0
    doorLoop = 0

    val = 1
    while val != cardVal:
        val = (val*7) % 20201227
        cardLoop += 1

    val = 1
    while val != doorVal:
        val = (val*7) % 20201227
        doorLoop += 1

    print(f"Card Loop = {cardLoop}")
    print(f"Door Loop = {doorLoop}")

    eKey = 1
    for i in range(cardLoop):
        eKey = (eKey * doorVal) % 20201227

    print(f"eKey = {eKey}")

    eKey = 1
    for i in range(doorLoop):
        eKey = (eKey * cardVal) % 20201227

    print(f"eKey = {eKey}")
