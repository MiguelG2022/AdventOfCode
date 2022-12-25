with open("daySixInput.txt", "r") as day6:
	lines = day6.readlines()

values = []
for i in lines: 
    values.append(i.replace("\n", ""))

packet = values[0]

def findStartOfPacket(packet):
    start = 0
    end = 4 
    while end < len(packet):
        interval = packet[start:end]
        unique = set(interval)
        if len(unique) == 4:
            return end
        start+=1
        end+=1
# Part One
print(findStartOfPacket(packet))


def findStartOfMessage(message):
    start = 0
    end = 14 
    while end < len(message):
        interval = message[start:end]
        unique = set(interval)
        if len(unique) == 14:
            return end
        start+=1
        end+=1

# Part Two 
print(findStartOfMessage(packet))


