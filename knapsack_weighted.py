import random

def s(S):
    return sum([e.s for e in S])

def v(S):
    return sum([e.v for e in S])

# def ks_max(elements):
#     max_element = max(elements,key=lambda x:x.v)
#     return set([(max_element)])

# def ks_greedy(elements):
#     l = list(elements)
#     l = sorted(l,key=lambda x:-x.v/x.s)
#     B = set()
#     for e in l:
#         if s(B) + e.s <= 1:
#             B.add(e)
#     return B

# def algorithm_B_offline(elements):
#     r = random.randint(1,2)

#     if r == 1:
#         return ks_max(elements)
#     else:
#         return ks_greedy(elements)
#     yield max_val,greedy_val

def ks_max(B,element):
    B.add(element)
    max_element = max(B,key=lambda x:x.v)
    Bprime = set([max_element])
    return Bprime

def ks_greedy(B,element):
    B.add(element)
    l = list(B)
    l = sorted(l,key=lambda x:-x.v/x.s)
    Bprime = set()
    for e in l:
        if s(Bprime) + e.s <= 1:
            Bprime.add(e)
    return Bprime

def algorithm_B(elements):
    r = random.randint(1,2)
    Bmax = set()
    Bgreedy = set()

    for element in elements:
        Bmax = ks_max(Bmax,element)
        Bgreedy = ks_greedy(Bgreedy,element)
        yield v(Bmax),v(Bgreedy)
