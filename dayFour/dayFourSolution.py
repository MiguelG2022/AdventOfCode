with open("dayFourInput.txt", "r") as day4:
	lines = day4.readlines()


for index, value in enumerate(lines):
    lines[index] = value.replace("\n", "").split(",")
    partOne = lines[index][0]
    partTwo = lines[index][1]
    lines[index][0] = partOne.split("-")
    lines[index][1] = partTwo.split("-")

for i, v in enumerate(lines):
    for index, value in enumerate(v):
        #['20', '93']
        integerValues = [eval(i) for i in value]
        lines[i][index] = integerValues


def countOverlap(times):
    count = 0
    for value in lines:
        partOne = value[0]
        partTwo = value[1]
        if partOne[0] <= partTwo[0] and partOne[1] >= partTwo[1]:
            count+=1
        elif partTwo[0] <= partOne[0] and partTwo[1] >= partOne[1]:
            count+=1
        else:
            continue
    return count 

def countOverlapTwo(times):
    count = 0
    for value in lines:
        value.sort()
        partOne = value[0]
        partTwo = value[1]
        if partOne[1] >= partTwo[0]:
            count +=1
    return count 

# Part One
print(countOverlap(lines))
# Part Two 
print(countOverlapTwo(lines))