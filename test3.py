from test2 import XorRotors, XorChipherLen, printBinary, printRotors, input, output, letterToIndex
from interchangeLogic import interchangeLogic

XorInput = []




for index, letter in enumerate(input):
    letterAsInt = letterToIndex[letter]
    C = [0]*5
    for i in range(5):
        C[i] = (letterAsInt >> i) & 1
    
    B = []
    for i, rotor in enumerate(XorRotors):
        B.append(rotor[index % XorChipherLen[i]])
    
    XorInput.append([C[j] ^ B[j] for j in range(5)])


rotorLens = [47,53,59,61,64,65,67,69,71,73]
XorChipherLen = [67, 61, 73, 59, 64]

interchangeRotorsLen = [47,53,65,69,71]

#Leta krockar genom att göra en ansats på första hjulet, testa sig fram osv
currRotorNum = 9
currGuess = 71

currRotor = ["#" for _ in range(currGuess)]

print(f"currRotorNum {currRotorNum}")
print(f"currGuess {currGuess}")

for index, binaryLetterInput in enumerate(XorInput):
    if sum(binaryLetterInput) == 1:
        letterAsInt = letterToIndex[output[index]]
        binaryLetterOutput = [0]*5
        for i in range(5):
            binaryLetterOutput[i] = (letterAsInt >> i) & 1
        start = binaryLetterInput.index(1)
        end = binaryLetterOutput.index(1)

        path = interchangeLogic(start, end)
        for step in path:
            rotorIndex, bit = step
            if currRotorNum == rotorIndex:
                curr = currRotor[index % currGuess]
                if curr != "#" and curr != bit:
                    print("Krock")
                    print(f"currRotorNum {currRotorNum}")
                    print(f"currGuess {currGuess}")
                    assert(0==1)
                else:
                    currRotor[index % currGuess] = bit


