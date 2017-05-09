import random

def s(S):
    return sum([e.s for e in S])

def ks_max(elements):
    max_element = max(elements,key=lambda x:x.v)
    return set([(max_element)])

def ks_greedy(elements):
    B = set()
    for e in elements:
        l = list(B)
        l.append(e)

        l = sorted(l,key=lambda x:-x.v/x.s)
        B = set()
        for element in l:
            if s(B) + e.s <= 1:
                B.add(e)
    return B

def algorithm_B(elements):
    r = random.randint(1,2)

    if r == 1:
        return ks_max(elements)
    else:
        return ks_greedy(elements)
