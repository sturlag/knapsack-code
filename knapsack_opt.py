def opt(E,i=0,c=1,memo={}):
    if c <= 0:
        return (set(), 0)
    if (i,c) in memo:
        return memo[(i,c)]
    if i == len(E)-1:
        if E[i].s <= c:
            return (set([E[i]]), E[i].s)
        else:
            return (set(), 0)
    (A,valA) = opt(E,i+1,c,memo) # don't include E[i]
    (B,valB) = opt(E,i+1, c-E[i].s,memo) # include E[i]
    B.add(E[i])
    valB += E[i].s
    if valB > c: # If it exceeds capacity, then no go.
        valB = 0
        B = set()
    if (valA < valB):
        memo[(i,c)] = (B, valB)
        return (B, valB)
    else:
        memo[(i,c)] = (A, valA)
        return (A, valA)
