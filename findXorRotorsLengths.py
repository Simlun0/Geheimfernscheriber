rotorLens = [47,53,59,61,64,65,67,69,71,73]
indexToLetter = "2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7"
letterToIndex = {}

for i, letter in enumerate(indexToLetter):
    letterToIndex[letter] = i

def printBinary(letter):
    letterAsInt = letterToIndex[letter]
    C = [0]*5
    for i in range(5):
        C[i] = (letterAsInt >> i) & 1
    ls = [str(c) for c in C]
    print(" ".join(ls))


def letterToBinary(letter):
    letterAsInt = letterToIndex[letter]
    C = [0]*5
    for i in range(5):
        C[i] = (letterAsInt >> i) & 1
    return C


f = open("gskrivin.txt")
input = f.read()

f = open("gskrivut.txt")
output = f.read()

def findXorRotorLengths(presentation=False):

    availablePositions = {}
    for length in rotorLens:
        availablePositions[length] = [True for _ in range(5)]

    for period in rotorLens:

        if presentation:
            print(period)

        sevenIndices = []
        sevenIndicesShift = []
        for index, letter in enumerate(output):
            if letter == "7":
                sevenIndices.append(index)
                sevenIndicesShift.append(index % period)



        for i, index in enumerate(sevenIndices):
            for j, jindex in enumerate(sevenIndices):
                if sevenIndicesShift[i] == sevenIndicesShift[j] and i < j:
                    if presentation:
                        print(f"shift = {sevenIndicesShift[i]}, i={index}, j={jindex}")
                        printBinary(input[index])
                        printBinary(input[jindex])
                        print()
                    
                    firstBinary = letterToBinary(input[index])
                    secondBinary = letterToBinary(input[jindex])

                    for bit in range(5):
                        if firstBinary[bit] != secondBinary[bit]:
                            availablePositions[period][bit] = False
    
    if presentation:
        for rotor in availablePositions:
            print(rotor)
            print(availablePositions[rotor])
    
    availableRotors = {}
    for pos in range(5):
        availableRotors[pos] = []
    
    for pos in range(5):
        for rotor in availablePositions:
            if availablePositions[rotor][pos]:
                availableRotors[pos].append(rotor)
    
    XorRotorLens = [None for _ in range(5)]

    while None in XorRotorLens:
        for pos in range(5):
            if len(availableRotors[pos]) == 1:
                rotor = availableRotors[pos][0]
                XorRotorLens[pos] = rotor
                for pos in range(5):
                    if rotor in availableRotors[pos]:
                        availableRotors[pos].remove(rotor)
    
    if presentation:
        print(XorRotorLens)
    
    return XorRotorLens


def main():
    findXorRotorLengths(presentation=True)


if __name__ == '__main__':
    main()