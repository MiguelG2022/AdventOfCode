# Reads data from Advent of Code 
with open("dayOneInput.txt", "r") as day1:
	lines = day1.readlines()

# Removes \n from data and also converts string into integers 
values = []
for i in lines: 
    stripped = i.replace("\n","")
    # values.append(stripped)
    if len(stripped)>0:
        values.append(int(stripped))
    else:
        values.append(stripped)
  

def getElfCalories(nums):
    count = 0
    res = []
    for num in nums:
        if num == "":
            res.append(count)
            count = 0
        else:
            count+=num 
    return res    
calories = getElfCalories(values)
def getElfMax(nums):
    return max(nums)

def getTopThree(nums):
    nums.sort(reverse=True)
    return nums[0] + nums[1] + nums[2]

# Part One
print(getElfMax(calories))
#Part Two 
print(getTopThree(calories))




