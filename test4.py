from test2 import XorRotors, XorChipherLen, printBinary, printRotors, input, output, letterToIndex
from interchangeLogic import interchangePathLogic, interchange

print("\n\n")

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

interchangeRotorsLen = [47,71,53,65,69]     # Rätt ordning

interchangeRotors = []

for length in interchangeRotorsLen:
    interchangeRotors.append(["#" for _ in range(length)])



for index, binaryLetterInput in enumerate(XorInput):
    if sum(binaryLetterInput) == 1 or sum(binaryLetterInput) == 4:
        letterAsInt = letterToIndex[output[index]]
        binaryLetterOutput = [0]*5
        for i in range(5):
            binaryLetterOutput[i] = (letterAsInt >> i) & 1
        if sum(binaryLetterInput) == 1:
            start = binaryLetterInput.index(1)
            end = binaryLetterOutput.index(1)
        else:
            start = binaryLetterInput.index(0)
            end = binaryLetterOutput.index(0)

        path = interchangePathLogic(start, end)
        for step in path:
            rotorIndex, bit = step
            curr = interchangeRotors[rotorIndex-5][index % interchangeRotorsLen[rotorIndex-5]]
            if curr != "#" and curr != bit:
                print("Krock")
            else:
                interchangeRotors[rotorIndex-5][index % interchangeRotorsLen[rotorIndex-5]] = bit

printRotors(interchangeRotors)
print()


for index, binaryLetterInput in enumerate(XorInput): 
    B = []
    for i, rotor in enumerate(interchangeRotors):
        B.append(rotor[index % interchangeRotorsLen[i]])
    
    if B.count("#") == 1:
        switchIndex = B.index("#")
        binaryLetterOutput = [0]*5
        letterAsInt = letterToIndex[output[index]]
        for i in range(5):
            binaryLetterOutput[i] = (letterAsInt >> i) & 1

        testBit = 0     #Gissning
        B[switchIndex] = testBit

        if index == 153:
            pass

        simulatedOutput_0 = binaryLetterInput.copy()
        
        interchange(B, simulatedOutput_0)

        testBit = 1                         
        B[switchIndex] = testBit
        simulatedOutput_1 = binaryLetterInput.copy()
        interchange(B, simulatedOutput_1)

        curr = interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]]

        if simulatedOutput_1 == simulatedOutput_0:
            pass
        elif binaryLetterOutput == simulatedOutput_0:
            testBit = 0
            if curr != "#" and curr != testBit:
                print("Krock")
                assert(1==0)
            else:
                interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]] = testBit
        elif binaryLetterOutput == simulatedOutput_1:
            if curr != "#" and curr != testBit:
                print("Krock")
                assert(1==0)
            else:
                interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]] = testBit
        else:
            print("Varken funkar!!")
            print(index)

printRotors(interchangeRotors)