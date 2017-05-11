from math import sqrt
from knapsack import s

t = (sqrt(5)-1)/2

S = lambda e: 0 < e.s < 2*t - 1
M = lambda e: 2*t - 1 <= e.s <= 1 - t
L = lambda e: 1 - t < e.s <= t
X = lambda e: t < e.s <= 1

def contains_only_S_and_M(B):
    for e in B:
        if L(e) or X(e):
            return False
    return True

def find_S_or_M(B):
    for e in B:
        if S(e) or M(e):
            return e
    return None

def find_L(B):
    for e in B:
        if L(e):
            return e
    return None

def iwama_taketomi(E):    
    B = set()
    for e in E:
        if s(B) > t:
            # approximation has been achieved
            break
        elif e.s + s(B) <= 1:
            B.add(e)
        else:
            # e is either L or X
            if X(e):
                B = set([e])
            else:
                # e is L
                if contains_only_S_and_M(B):
                    B.add(e)
                    while s(B) > 1:
                        elem = find_S_or_M(B)
                        if elem is None:
                            raise Exception("No S or M element found")
                        B.remove(elem)
                else:
                    # B contains an L and 0 or more S
                    l = find_L(B)
                    if l is None:
                        raise Exception("No L element found")
                    if e.s + l.s <= 1:
                        B = set([e, l])
                    elif e.s < l.s:
                        B.remove(l)
                        B.add(e)
                    else:
                        pass
                        # do nothing
                        # i.e. discards e
    
    return (B, s(B))
