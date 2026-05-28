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



for i, letter in enumerate(indexToLetter):
    letterToIndex[letter] = i

def letterToBinary(letter):
    letterAsInt = letterToIndex[letter]
    C = [0]*5
    for i in range(5):
        C[i] = (letterAsInt >> i) & 1
    ls = [str(c) for c in C]
    print(" ".join(ls))

f = open("gskrivin.txt")
input = f.read()

f = open("gskrivut.txt")
output = f.read()

XorChipherLen = [67, 61, 73, 59, 64]
XorRotors = []

for length in XorChipherLen:
    XorRotors.append(["#" for _ in range(length)])

print(output.count("7"))

for period in rotorLens:

    print(period)

    sevenIndices = []
    for index, letter in enumerate(output):
        if letter == "7":
            sevenIndices.append(index)


    for index in sevenIndices:
        letter = input[index]
        letterAsInt = letterToIndex[letter]
        C = [0]*5
        for i in range(5):
            C[i] = (letterAsInt >> i) & 1

        for i, bit in enumerate(C):
            curr = XorRotors[i][index % XorChipherLen[i]]
            correct = 1 - bit
            if curr != "#" and correct != curr:
                print("Katastrofiskt fel")
            else:
                XorRotors[i][index % XorChipherLen[i]] = correct

print(output.count("2"))

for period in rotorLens:

    print(period)

    twoIndices = []
    for index, letter in enumerate(output):
        if letter == "2":
            twoIndices.append(index)




    for index in twoIndices:
        letter = input[index]
        letterAsInt = letterToIndex[letter]
        C = [0]*5
        for i in range(5):
            C[i] = (letterAsInt >> i) & 1

        for i, bit in enumerate(C):
            curr = XorRotors[i][index % XorChipherLen[i]]
            correct = bit
            if curr != "#" and correct != curr:
                print("Katastrofiskt fel")
            else:
                XorRotors[i][index % XorChipherLen[i]] = correct


printRotors(XorRotors)


for index in range(len(input)):
    B = []
    for i, rotor in enumerate(XorRotors):
        B.append(rotor[index % XorChipherLen[i]])
    
    if B.count("#") == 1:
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
        XorRotors[rotorIndexSwitch][index % XorChipherLen[rotorIndexSwitch]] = diff ^ C[rotorIndexSwitch]
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

printRotors(XorRotors)