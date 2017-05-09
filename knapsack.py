import random
from itertools import chain, combinations

class Element:

    def __init__(self,s,v):
        self.s = s
        self.v = v

    def __str__(self):
        return 'Element[s='+str(self.s)+',v='+str(self.v)+']'

def s(S):
    return sum([e.s for e in S])

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

S = lambda s: 0.0 <= s <= 0.3
M1 = lambda s: 0.3 < s <= 0.4
M2 = lambda s: 0.4 < s <= 0.5
M3 = lambda s: 0.5 < s < 0.6
M4 = lambda s: 0.6 <= s < 0.7
M = lambda s: 0.3 < s < 0.7
L = lambda s: s >= 0.7

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
        output = set([str(B1) for e in B1]), s(B1)
    else:
        output = set([str(B2) for e in B2]), s(B2)
    return output

def algorithm_A(E):
    B = set()
    B1 = set()
    B2 = set()

    f = 0
    r = random.randint(1,2)
    for e in E:
        if L(e.s):
            B = set([e])
            return B,s(B)
        if M4(e.s):
            f = 1

        B1 = A1(f,B1,e)
        B2 = A2(f,B2,e)

        # if 0.5*(s(B1) + s(B2)) >= 0.7:
        #     break

    # if r == 1:
    #     return B1,s(B1)
    # else:
    #     return B2,s(B2)

    return B1,B2,s(B1),s(B2)

def A1(f,B1,e):
    newB1 = set()
    B1.add(e)
    if f == 0:
        #Find smallest element in M3
        element = smallest(B1,M3)
    else:
        #Find smallest element in M4
        element = smallest(B1,M4)

    if element != None:
        newB1.add(element)

    B1 = list(B1)
    B1 = sorted(B1,key=lambda e:-e.s)

    for e in B1:
        if s(newB1) + e.s <= 1:
            newB1.add(e)
    return newB1

def A2(f,B2,e):
    newB2 = set()
    B2.add(e)

    I_found = False

    if f == 0:
        I = containsValue(B2,0.9)
        if I:
            newB2 = I
            I_found = True

    elif f == 1:
        I = containsValue(B2,0.8)
        if I:
            newB2 = I
            I_found = True
    if not I_found:
        B2 = list(B2)
        #Find smallest element in M2
        element = smallest(B2,M2)
        if element != None:
            newB2.add(element)

        #Find smallest element in M1
        element = smallest(B2,M1)
        if element != None:
            newB2.add(element)

        #Add medium items from smallest to largest
        medium = sorted([e for e in B2 if M(e.s)],key=lambda e: e.s)
        for element in medium:
            if s(newB2) + element.s <= 1:
                newB2.add(element)

        #Add small items from largest to smallest
        small = sorted([e for e in B2 if S(e.s)],key=lambda e: -e.s)
        for element in small:
            if s(newB2) + element.s <= 1:
                newB2.add(element)
    return newB2

def smallest(S,func):
    smallest = None
    for e in S:
        if func(e.s):
            if smallest == None:
                smallest = e
            else:
                if e.s < smallest.s:
                    smallest = e
    return smallest

def containsValue(S,t):
    B_l = set([e for e in S if e.s > 1-t])
    B_s = set([e for e in S if e.s <= 1-t])

    for C in powerset(B_l):
        if s(C) + s(B_s) >= t and s(C) <= 1:
            I = set(C)
            for e in B_s:
                if s(I) + e.s <= 1:
                    I.add(e)
            return I
    return None
