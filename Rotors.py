standardRotorLens = [47,53,59,61,64,65,67,69,71,73]

def TrivialRotors(rotorLens=standardRotorLens): 
    Rotors = []

    for len in rotorLens:
        Rotors.append([0]*len)

    return Rotors
