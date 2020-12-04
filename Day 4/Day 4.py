# passportProcessing : check validity of passport entries from input file
def passportProcessing():
    with open("Day 4 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    fieldsValid = 0
    valsValid = 0
    tmp = []
    arr = []
    for i in range(len(lines)):
        curr = lines[i]
        if curr == '\n':
            arr.append(tmp)
            tmp = []
        else:
            curr = lines[i].split(" ")
            tmp += curr
    # print(arr)
    for i in range(len(arr)):
        fields = {}
        p = arr[i]
        for j in range(len(p)):
            field = p[j]
            pair = field.split(":")
            fields[pair[0]] = pair[1]
        fs = list(fields.keys())
        if(("byr" in fs) and ("iyr" in fs) and ("eyr" in fs) and
           ("hgt" in fs) and ("hcl" in fs) and ("ecl" in fs) and
           ("pid" in fs)):
            # contains all required fields
            fieldsValid += 1

            # get values of each fields
            byr = fields["byr"].split("\n")[0]
            iyr = fields["iyr"].split("\n")[0]
            eyr = fields["eyr"].split("\n")[0]
            hgt = fields["hgt"].split("\n")[0]
            hcl = fields["hcl"].split("\n")[0]
            ecl = fields["ecl"].split("\n")[0]
            pid = fields["pid"].split("\n")[0]

            # check validity of values
            if((1920 <= int(byr) <= 2002) and
               (2010 <= int(iyr) <= 2020) and
               (2020 <= int(eyr) <= 2030) and
               (((hgt[-2:] == "cm") and (150 <= int(hgt[:-2]) <= 193)) or
                ((hgt[-2:] == "in") and (59 <= int(hgt[:-2]) <= 76))) and
               ((hcl[0] == "#") and (len(hcl[1:]) == 6) and isChars(hcl[1:])) and
               (ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and
               ((len(pid) == 9) and isDigits(pid))):
                valsValid += 1
    return (fieldsValid, valsValid)

# isChars : check if a string contains 0-9 or a-f ONLY
def isChars(txt):
    for x in txt:
        if ( not ( (97 <= ord(x) <= 102) or (48 <= ord(x) <= 57))):
            return False
    return True

# isDigits : check if a string contains 0-9 ONLY
def isDigits(txt):
    for x in txt:
        if(not(48 <= ord(x) <= 57)):
            return False
    return True
