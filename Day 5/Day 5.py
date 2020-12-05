# boardingPasses : process seat locations based on list of boarding passes, find
#                  maximum seatID and my seatID
def boardingPasses():
    with open("Day 5 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    seat_ids = []
    for i in range(len(lines)):
        cur_pass = lines[i]

        # sequence of F's and B's (length = 7)
        fb = cur_pass[:7]

        # sequence of F's and B's (length = 3)
        lr = cur_pass[7:]

        # get the seat row number
        fr = 0
        ba = 127
        for i in range(0,6):
            if fb[i] == 'F':
                ba -= (ba - fr + 1)/2
            else:
                fr += (ba - fr + 1)/2
        if fb[6] == 'F':
            ba = fr
        else:
            fr = ba

        # get the seat col number
        l = 0
        r = 7
        for i in range(0,2):
            if lr[i] == 'L':
                r -= (r - l + 1)/2
            else:
                l += (r - l + 1)/2
        if lr[2] == 'L':
            r = l
        else:
            l = r

        # append seat ID to array seat_ids
        seat_ids.append(int((fr * 8) + l))

    # part 1
    print(f"Max ID = {max(seat_ids)}")

    # part 2
    for i in range(min(seat_ids), max(seat_ids) + 1):
        if((i not in seat_ids) and (i-1 in seat_ids) and (i+1 in seat_ids)):
            print(f"My ID = {i}")

    return
                
