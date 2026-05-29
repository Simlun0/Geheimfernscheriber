from findXorRotors import printBinary, printRotors, input, output, letterToIndex, findXorRotors, letterToBinary
from findXorRotorsLengths import findXorRotorLengths
from findInterchangeRotorsLength import findInterchangeRotorsLength
from interchangeLogic import interchangePathLogic, interchange

XorInput = []

def findInterchangeRotors(presentation=False):

    XorRotors = findXorRotors()
    XorRotorsLens = findXorRotorLengths()

    for index, letter in enumerate(input):
        C = letterToBinary(letter)
        
        B = []
        for i, rotor in enumerate(XorRotors):
            B.append(rotor[index % XorRotorsLens[i]])
        
        XorInput.append([C[j] ^ B[j] for j in range(5)])

    interchangeRotorsLen = findInterchangeRotorsLength()

    interchangeRotors = []

    for length in interchangeRotorsLen:
        interchangeRotors.append(["#" for _ in range(length)])

    for index, binaryLetterInput in enumerate(XorInput):
        if sum(binaryLetterInput) == 1 or sum(binaryLetterInput) == 4:
            binaryLetterOutput = letterToBinary(output[index])
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
                    raise Exception("Ömsesidigt uteslutande krav!")
                else:
                    interchangeRotors[rotorIndex-5][index % interchangeRotorsLen[rotorIndex-5]] = bit

    if presentation:
        printRotors(interchangeRotors)
        print()


    for index, binaryLetterInput in enumerate(XorInput): 
        B = []
        for i, rotor in enumerate(interchangeRotors):
            B.append(rotor[index % interchangeRotorsLen[i]])
        
        if B.count("#") == 1:
            switchIndex = B.index("#")
            binaryLetterOutput = letterToBinary(output[index])

            testBit_0 = 0     #Gissning
            B[switchIndex] = testBit_0

            simulatedOutput_0 = binaryLetterInput.copy()
            
            interchange(B, simulatedOutput_0)

            testBit_1 = 1                         
            B[switchIndex] = testBit_1
            simulatedOutput_1 = binaryLetterInput.copy()
            interchange(B, simulatedOutput_1)

            curr = interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]]

            if simulatedOutput_1 == simulatedOutput_0:
                pass
            elif binaryLetterOutput == simulatedOutput_0:
                if curr != "#" and curr != testBit_0:
                    raise Exception("Ömsesidigt uteslutande krav!")
                else:
                    interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]] = testBit_0
            elif binaryLetterOutput == simulatedOutput_1:
                if curr != "#" and curr != testBit_1:
                    raise Exception("Ömsesidigt uteslutande krav!")
                else:
                    interchangeRotors[switchIndex][index % interchangeRotorsLen[switchIndex]] = testBit_1
            else:
                raise Exception("Varken funkar!")

    if presentation:
        printRotors(interchangeRotors)
    
    return interchangeRotors


def main():
    findInterchangeRotors(presentation=True)


if __name__ == '__main__':
    main()