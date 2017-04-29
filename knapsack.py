import random

class Element:

    def __init__(self,s,v):
        self.s = s
        self.v = v

def twobins(E):
    B1 = set()
    B2 = set()

    for e in E:
        if s(B1) + e.s <= 1:
            B1.add(e)
        elif s(B2) + e.s <= 1:
            B2.add(e)

    r = random.randint(1,2)
    if r == 1:
        return B1,s(B1)
    else:
        return B2,s(B2)

def s(S):
    return sum([e.s for e in S])
