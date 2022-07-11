
def generateDarkerColour(currentIndex, totalIndex):
    darkestColour = 0.25
    constant = 1/1.5
    offset = currentIndex**constant
    maxValue = totalIndex**constant
    multiplier = (maxValue - offset)/maxValue
    # offset = ((totalIndex - currentIndex + 1)**2) / ((totalIndex + 1)**2)
    # multiplier = (darkestColour * offset + (1 - darkestColour)) * darkestColour + darkestColour - 1

    variableNames = ["offset", "currentIndex", "totalIndex", "multiplier"]
    variables = [offset, currentIndex, totalIndex, multiplier]
    for x in range(len(variables)):
        print("{0}: {1}".format(variableNames[x], variables[x]))
    print("\n")
    return multiplier


def genMultiplierList(size):
    multipliersList = []
    constant = 0.5
    darkestColour = 0.25
    maxValue = size**constant
    for j in range(size):
        value = 1 - (j**constant / maxValue)
        multipliersList.append(value)

    oldRange = 1 - 0
    newRange = 1 - darkestColour
    for j in range(size):
        multipliersList[j] = (((multipliersList[j]) * newRange) / oldRange) + darkestColour
    return multipliersList


# main
multipliers = genMultiplierList(5)
print(str(genMultiplierList(5)) + "\n")

for i in range(len(multipliers) - 1):
    print(multipliers[i] - multipliers[i + 1])
