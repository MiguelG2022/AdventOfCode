with open("dayTwoInput.txt", "r") as day2:
	lines = day2.readlines()

values = []
for i in lines: 
    value = i.replace("\n", "")
    final = value.split()
    values.append(final)


def calculate_score(games):
    total_score = 0
    for opponent, you in games:
        #draw 
        if (opponent == "A" and you == "X") or (opponent == "B" and you == "Y") or (opponent == "C" and you == "Z"):
            if you == "X":
                total_score += 1 + 3
            elif you == "Y":
                total_score += 2 + 3
            else:
                total_score += 3 + 3
        #loss
        elif (opponent == "A" and you == "Z") or (opponent == "B" and you == "X") or (opponent == "C" and you == "Y"):
            if you == "X":
                total_score += 1 + 0
            elif you == "Y":
                total_score += 2 + 0
            else:
                total_score += 3 + 0
        #win
        else:
            if you == "X":
                total_score += 1 + 6
            elif you == "Y":
                total_score += 2 + 6
            else:
                total_score += 3 + 6
    return total_score

#Part One 
print(calculate_score(values))

def new_strategy(games):
    total_score = 0
    for opponent, result in games:
        if result == "X":
            if opponent == "A":
                total_score += 0 + 3
            elif opponent == "B":
                total_score += 0 + 1
            else:
                total_score += 0 + 2
        elif result == "Y":
            if opponent == "A":
                total_score += 3 + 1
            elif opponent == "B":
                total_score += 3 + 2
            else:
                total_score += 3 + 3
        else: 
            if opponent == "A":
                total_score += 6 + 2
            elif opponent == "B":
                total_score += 6 + 3
            else:
                total_score += 6 + 1
    return total_score

#Part Two 
print(new_strategy(values))

