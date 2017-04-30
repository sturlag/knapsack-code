def opt(E,i=0,c=1,memo={}):
    print memo
    if (i,c) in memo:
        return memo[(i,c)]
    if i == len(E)-1:
        if E[i].s <= c:
            return (set([E[i]]), E[i].s)
        else:
            return (set(), 0)
    (A,valA) = opt(E,i+1,c,memo) # don't include E[i]
    (B, valB) = opt(E,i+1, c-E[i].s,memo) # include E[i]
    if (valA < valB + E[i].s):
        B.add(E[i])
        memo[(i,c)] = (B, valB + E[i].s)
        return (B, valB + E[i].s)
    else:
        memo[(i,c)] = (A, valA)
        return (A, valA)
