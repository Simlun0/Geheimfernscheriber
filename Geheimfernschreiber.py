from solution import Rotors

f = open("gskrivin.txt")
msg = f.read()

f = open("gskrivut.txt")
output = f.read()

indexToLetter = "2T3O4HNM5LRGIPCVEZDBSYFXAWJ6UQK7"
letterToIndex = {}

for i, letter in enumerate(indexToLetter):
    letterToIndex[letter] = i


class Geheimfernscheriber():
    def __init__(self, rotors=Rotors):
        self.rotors = rotors

        self.shift = [0]*len(rotors)

    
    def interchange(self, a, b, list):
        temp = list[a]
        list[a] = list[b]
        list[b] = temp

    def encryptLetter(self, letter):
        letterAsInt = letterToIndex[letter]
        ecrLetterAsInt = self.encryptLetterInts(letterAsInt)
        return indexToLetter[ecrLetterAsInt]

    def encryptLetterInts(self, letter):
        B = [self.rotors[i][self.shift[i]] for i in range(len(self.rotors))]
        C = [0]*5
        for i in range(5):
            C[i] = (letter >> i) & 1
        
        
        for i in range(5):
            C[i] = C[i] ^ B[i]

        if B[5]:
            self.interchange(0,4,C)

        if B[6]:
            self.interchange(0,1,C)

        if B[7]:
            self.interchange(1,2,C)

        if B[8]:
            self.interchange(2,3,C)

        if B[9]:
            self.interchange(3,4,C)

        outLetter = 0
        for i in range(5):
            outLetter += C[i]<<i

        self.updateRotors()

        return outLetter



    def updateRotors(self):
        for i in range(len(self.rotors)):
            self.shift[i] = (self.shift[i] + 1) % len(self.rotors[i])
        
    

    def encrypt(self, message):
        ecrMessage = ""
        for letter in message:
            letterAsInt = letterToIndex[letter]
            ecrLetterAsInt = self.encryptLetterInts(letterAsInt)
            ecrLetter = indexToLetter[ecrLetterAsInt]
            ecrMessage += ecrLetter

        return ecrMessage


def main():
    machine = Geheimfernscheriber()

    print(machine.encrypt(output))



if __name__ == '__main__':
    main()