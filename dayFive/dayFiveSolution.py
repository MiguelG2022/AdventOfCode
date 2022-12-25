with open("dayFiveInput.txt", "r") as day5:
	lines = day5.readlines()

values = []
for i in lines: 
    values.append(i.replace("\n", ""))
for index,value in enumerate(values):
    values[index] = value.split(",")
commands = values[10:]
for index, value in enumerate(commands):
    current = []
    for g in value[0]:
        if g.isdigit():
            current.append(g)
    commands[index]=current


stack1 = ["D","T","W","F","J","S","H","N"]
stack2 = ["H","R","P","Q","T","N","B","G"]
stack3 = ["L","Q","V"]
stack4 = ["N","B","S","W","R","Q"]
stack5 = ["N","D","F","T","V","M","B"]
stack6 = ["M","D","B","V","H","T","R"]
stack7 = ["D","B","Q","J"]
stack8 = ["D","N","J","V","R","Z","H","Q"]
stack9 = ["B","N","H","M","S"]


stacks = [
    ["D","T","W","F","J","S","H","N"],
    ["H","R","P","Q","T","N","B","G"],
    ["L","Q","V"],
    ["N","B","S","W","R","Q"],
    ["N","D","F","T","V","M","B"],
    ["M","D","B","V","H","T","R"],
    ["D","B","Q","J"],
    ["D","N","J","V","R","Z","H","Q"],
    ["B","N","H","M","S"],
]
def topOfStacks(stacks, commands):
    for index, command in enumerate(commands):
        moveString = "".join(command[0:-2])
        moveInt = int(moveString)
        stackFromString = "".join(command[-2])
        stackFromInt = int(stackFromString)-1 
        stackToString = "".join(command[-1])
        stackToInt = int(stackToString)-1
        cratesToMove = []
        stackF = stacks[stackFromInt]
        stackT = stacks[stackToInt]
        for _ in range(moveInt):
            crate = stackF.pop()
            stackT.append(crate)
        stacks[stackFromInt] = stackF
        stacks[stackToInt] = stackT

    return stacks


#Part One 
newStacks= topOfStacks(stacks, commands)
results = []
for i in newStacks:
    if i:
        results.append(i.pop())
print(results)
  

def topOfStacksTwo(stacks, commands):
    for index, command in enumerate(commands):
        moveString = "".join(command[0:-2])
        moveInt = int(moveString)
        stackFromString = "".join(command[-2])
        stackFromInt = int(stackFromString)-1 
        stackToString = "".join(command[-1])
        stackToInt = int(stackToString)-1        
        stackF = stacks[stackFromInt]
        stackT = stacks[stackToInt]
        cratesToMove = stackF[-moveInt:]
        for _ in range(moveInt):
            stackF.pop()
        stacks[stackFromInt] = stackF
        stacks[stackToInt] = stackT + cratesToMove

    return stacks

stacksTwo = [
    ["D","T","W","F","J","S","H","N"],
    ["H","R","P","Q","T","N","B","G"],
    ["L","Q","V"],
    ["N","B","S","W","R","Q"],
    ["N","D","F","T","V","M","B"],
    ["M","D","B","V","H","T","R"],
    ["D","B","Q","J"],
    ["D","N","J","V","R","Z","H","Q"],
    ["B","N","H","M","S"],
]

#Part Two 
newStacksTwo= topOfStacksTwo(stacksTwo, commands)
resultsTwo = []
for i in newStacksTwo:
    if i:
        resultsTwo.append(i.pop())
print("".join(resultsTwo))
print(resultsTwo)

