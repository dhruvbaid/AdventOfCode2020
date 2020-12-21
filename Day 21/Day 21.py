# intersect : returns intersection of 2 lists
def intersect(l1: list, l2: list):
    res = []
    for x in l1:
        if x in l2:
            res.append(x)
    return res

# main : put all allergens into a dictionary, intersect the ingredients they
#        might have come from repeatedly to get the final plausible list of
#        ingredients corresponding to each allergen, remove singular ingredients
#        repeatedly until everything is singular, and obtain the one-to-one map
#        from allergen to ingredient. The rest is simple.
def main():
    with open("Day 21 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character at the end of each line
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]

    # --------------------------------- PART 1 ---------------------------------
    # convert lines to a list [[[ingredients], [allergens]], ..., [[],[]]]
    for i in range(len(lines)):
        lines[i] = lines[i].split(" (contains ")
        lines[i][0] = lines[i][0].split(" ")
        lines[i][1] = lines[i][1][:-1].split(", ")

    # create a dictionary {allergen: [possible ingredients]}
    d = dict()
    for l in lines:
        for allergen in l[1]:
            if allergen in d:
                d[allergen] = intersect(d[allergen], l[0])
            else:
                d[allergen] = l[0]

    # remove singular values
    valid = 1
    while valid == 1:
        valid = 0
        for allergen in d:
            if len(d[allergen]) == 1:
                for otherAllergen in d:
                    if otherAllergen != allergen:
                        if d[allergen][0] in d[otherAllergen]:
                            d[otherAllergen].remove(d[allergen][0])
                            valid = 1

    # get list of unsafe ingredients
    unsafeI = []
    for allergen in d:
        for ing in d[allergen]:
            if ing not in unsafeI:
                unsafeI.append(ing)

    # get set of all ingredients from lines
    ingredients = set()
    for l in lines:
        for x in l[0]:
            ingredients.add(x)

    # get list of safe ingredients
    safeI = []
    for ing in ingredients:
        if ing not in unsafeI:
            safeI.append(ing)

    # get the total count of safe ingredients
    count = 0
    for ing in safeI:
        for l in lines:
            if ing in l[0]:
                count += 1

    print(f"Part 1: {count}")

    # --------------------------------- PART 2 ---------------------------------
    # sort unsafe ingredients in alphabetical order of their allergens
    allKeys = list(d.keys())
    allVals = list(d.values())
    for i in range(len(allVals)):
        allVals[i] = allVals[i][0]
        
    for i in range(len(unsafeI)):
        unsafeI[i] = [unsafeI[i], allKeys[allVals.index(unsafeI[i])]]

    unsafeI = sorted(unsafeI, key = lambda x: x[1])

    # combine unsafe ingredients into a single comma-separated string
    p2 = ""
    for ing in unsafeI:
        p2 += ing[0]
        p2 += ","
    p2 = p2[:-1]
    
    print(f"Part 2: {p2}")
    
    return
