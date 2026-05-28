#   Katastrofkod men lättaste sättet med alla specialfall

def interchangePathLogic(start, end):
    if start == 0:
        if end == 0:
            return [(5,0), (6,0)]
        if end == 1:
            return [(5,0), (6,1), (7,0)]
        if end == 2:
            return [(5,0), (6,1), (7,1), (8,0)]
        if end == 3:
            return []
        if end == 4:
            return []
    
    if start == 1:
        if end == 0:
            return [(6,1)]
        if end == 1:
            return [(6,0), (7,0)]
        if end == 2:
            return [(6,0), (7,1), (8,0)]
        if end == 3:
            return [(6,0), (7,1), (8,1), (9,0)]
        if end == 4:
            return [(6,0), (7,1), (8,1), (9,1)]

    if start == 2:
        if end == 0:
            print("Omöjligt!")
            print(start, end)
            return []
        if end == 1:
            return [(7,1)]
        if end == 2:
            return [(7,0), (8,0)]
        if end == 3:
            return [(7,0), (8,1), (9,0)]
        if end == 4:
            return [(7,0), (8,1), (9,1)]
        
    if start == 3:
        if end == 0:
            print("Omöjligt!")
            print(start, end)
            return []
        if end == 1:
            print("Omöjligt!")
            print(start, end)
            return []
        if end == 2:
            return [(8,1)]
        if end == 3:
            return [(8,0), (9,0)]
        if end == 4:
            return [(8,0), (9,1)]
        
    if start == 4:
        if end == 0:
            return [(5,1), (6,0)]
        if end == 1:
            return [(5,1), (6,1), (7,0)]
        if end == 2:
            return [(5,1), (6,1), (7,1), (8,0)]
        if end == 3:
            return []
        if end == 4:
            return []


def interchangeInstance(a, b, list):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp


def interchange(bits, input):
    if bits[0]:
        interchangeInstance(0,4,input)

    if bits[1]:
        interchangeInstance(0,1,input)

    if bits[2]:
        interchangeInstance(1,2,input)

    if bits[3]:
        interchangeInstance(2,3,input)

    if bits[4]:
        interchangeInstance(3,4,input)