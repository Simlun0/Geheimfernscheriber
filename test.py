rotorLens = [47,53,59,61,64,65,67,69,71,73]
indexToLetter = "2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7"
letterToIndex = {}

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

period = 59

indices = []
for index, char in enumerate(input):
    if char == "2":
        indices.append(index)

print(indices)
interestingPoints = []

for i in indices:
    iShift = i % period
    for j in indices:
        jShift = j % period
        if iShift == jShift and i < j:
            print(i, j)
            if i not in interestingPoints:
                interestingPoints.append(i)
            if j not in interestingPoints:
                interestingPoints.append(j)


for point in interestingPoints:
    ecrletter = output[point]
    letterToBinary(input[point])
    letterToBinary(ecrletter)
    print()


lim = 32

for letter in input:
    if letterToIndex[letter] >= lim:
        print(f"Större än {lim}")


# for i in range(len(input)):
#     if input[i] == output[i]:
#         print(i)

print(output.count("7"))


period = 73

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
            print(f"shift = {sevenIndicesShift[i]}, i={index}, j={jindex}")
            letterToBinary(input[index])
            letterToBinary(input[jindex])
            print()



# for i, index in enumerate(sevenIndices):
#     letterToBinary(input[index])
#     if i+1 < len(sevenIndices):
#         print()

print(output.count("2"))