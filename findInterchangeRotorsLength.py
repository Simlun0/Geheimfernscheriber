from findXorRotors import printBinary, printRotors, input, output, letterToIndex, findXorRotors, findXorRotorLengths, letterToBinary, rotorLens
from interchangeLogic import *

XorInput = []

def findInterchangeRotorsLength(presentation=False):

    XorRotors = findXorRotors()
    XorRotorsLens = findXorRotorLengths()

    for index, letter in enumerate(input):
        C = letterToBinary(letter)
        
        B = []
        for i, rotor in enumerate(XorRotors):
            B.append(rotor[index % XorRotorsLens[i]])
        
        XorInput.append([C[j] ^ B[j] for j in range(5)])


    interchangeRotorsLen = []
    for length in rotorLens:
        if length not in XorRotorsLens:
            interchangeRotorsLen.append(length)

    if presentation:
        print("Möjliga permutations hjul:", interchangeRotorsLen)

    #Leta krockar genom att göra en ansats på första hjulet, testa sig fram osv

    availablePositions = {}
    for length in interchangeRotorsLen:
        availablePositions[length] = [True for _ in range(5)]

    for length in interchangeRotorsLen:
        for rotorPos in range(5):

            currRotor = ["#" for _ in range(length)]

            for index, binaryLetterInput in enumerate(XorInput):
                if sum(binaryLetterInput) == 1:
                    letterAsInt = letterToIndex[output[index]]
                    binaryLetterOutput = [0]*5
                    for i in range(5):
                        binaryLetterOutput[i] = (letterAsInt >> i) & 1
                    start = binaryLetterInput.index(1)
                    end = binaryLetterOutput.index(1)

                    path = interchangePathLogic(start, end)
                    for step in path:
                        rotorIndex, bit = step
                        if rotorPos == rotorIndex-5:
                            curr = currRotor[index % length]
                            if curr != "#" and curr != bit:
                                if presentation:
                                    print(f"Krock! Hjul {length} kan inte vara på position {rotorPos}")

                                availablePositions[length][rotorPos] = False

                            else:
                                currRotor[index % length] = bit
    
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
    findInterchangeRotorsLength(presentation=True)


if __name__ == '__main__':
    main()