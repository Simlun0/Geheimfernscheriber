from findXorRotorsLengths import findXorRotorLengths

rotorLens = [47,53,59,61,64,65,67,69,71,73]
indexToLetter = "2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7"
letterToIndex = {}

def printRotors(rotors):
    for rotor in rotors:
        print(", ".join([str(ele) for ele in rotor]))

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


for i, letter in enumerate(indexToLetter):
    letterToIndex[letter] = i


f = open("gskrivin.txt")
input = f.read()

f = open("gskrivut.txt")
output = f.read()

XorRotorLens = findXorRotorLengths()

def findXorRotors(presentation=False):
    XorRotors = []

    for length in XorRotorLens:
        XorRotors.append(["#" for _ in range(length)])

    if presentation:
        print("Amount of all 0's in output:", output.count("2"))
        print("Amount of all 1's in output:", output.count("7"))

    for char in ["7", "2"]:
        specialIndices = []
        for index, letter in enumerate(output):
            if letter == char:
                specialIndices.append(index)


        for index in specialIndices:
            letter = input[index]

            for i, bit in enumerate(letterToBinary(letter)):
                curr = XorRotors[i][index % XorRotorLens[i]]
                if char == "7":
                    correct = 1 - bit
                else:
                    correct = bit

                if curr != "#" and correct != curr:
                    raise Exception("Ömsesidigt uteslutande krav!")
                else:
                    XorRotors[i][index % XorRotorLens[i]] = correct

    if presentation:
        printRotors(XorRotors)


    for index in range(len(input)):
        B = []
        for i, rotor in enumerate(XorRotors):
            B.append(rotor[index % XorRotorLens[i]])
        
        if B.count("#") == 1:
            if presentation:
                print(f"index: {index}")

            rotorIndexSwitch = B.index("#")
            inpLetter = letterToIndex[input[index]]
            outLetter = letterToIndex[output[index]]

            C = [0]*5
            D = [0]*5
            for i in range(5):
                C[i] = (inpLetter >> i) & 1

            inpSum = 0
            for i in range(5):
                if i != rotorIndexSwitch:
                    inpSum += B[i] ^ C[i]
                    D[i] = B[i] ^ C[i]
                else:
                    D[i] = "?"

            outInp = sum([(outLetter >> j) & 1 for j in range(5)])

            diff = abs(inpSum-outInp)       # Vi har ekvationen # ^ C[switchIndex] = diff vilket ger # = diff ^ C[switchIndex]
            XorRotors[rotorIndexSwitch][index % XorRotorLens[rotorIndexSwitch]] = diff ^ C[rotorIndexSwitch]
            if presentation:
                print("Input:   ", end="")
                printBinary(input[index])
                print("Xor:     ", end="")
                ls = [str(d) for d in D]
                print(" ".join(ls))
                print("Output:  ", end="")
                printBinary(output[index])
                print(f"Matrix B: {B}")
                print(f"rotorIndexSwitch {rotorIndexSwitch}")
                print(f"sol: {diff ^ C[rotorIndexSwitch]}")
                print()

    if presentation:
        printRotors(XorRotors)
    
    return XorRotors


def main():
    findXorRotors(presentation=True)


if __name__ == '__main__':
    main()