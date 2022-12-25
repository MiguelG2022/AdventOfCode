with open("dayThreeInput.txt", "r") as day3:
	lines = day3.readlines()

values = []

for i in lines: 
    values.append(i.replace("\n", ""))

# Calculates the priority of an item 
def worth(s):
    if s.islower():
        return ord(s) - ord("a") + 1 
    else:
        return ord(s) - ord("A") + 27

# calculates the sum of all priorities 
def sumOfPriorities(ruckSacks):
    ruckSackSplit = []
    for example in ruckSacks:
        part1 = example[0:len(example)//2]
        part2 = example[len(example)//2:]
        ruckSackSplit.append([part1]+[part2])

    priorities = []
    for part1, part2 in ruckSackSplit:
        current=[]
        unique = set(part1)
        for i in part2:
            if i in unique:
                priorities.append(i)
                break
    totalScore = 0
    for i in priorities:
        totalScore += worth(i)

    return totalScore 
#PartOne
print(sumOfPriorities(values))  


groupsOfThree = list(zip(*[iter(values)]*3))
# finds total score
def find_score(sack):
    total = 0 
    for i in sack: 
        part = i[0]
        part2 = i[1]
        part3 = i[2]
        overlap = find_unique(part, part2, part3)
        total += worth(overlap) 

    return total 


# finds unique value in the three sacks 
def find_unique(list1, list2, list3):
    overlap1 = set(list1)
    overlap2 = set()
    overlap3 = set()
    for i in list2:
        if i in overlap1:
            overlap2.add(i)
    
    for z in list3:
        if z in overlap2 and z in overlap1:
            res = z 

    return res
# Part Two 
print(find_score(groupsOfThree))