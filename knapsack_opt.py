# def opt(E,i=0,c=1,memo={}):
#     if c <= 0:
#         return (set(), 0)
#     if (i,c) in memo:
#         return memo[(i,c)]
#     if i == len(E)-1:
#         if E[i].s <= c:
#             return (set([E[i]]), E[i].s)
#         else:
#             return (set(), 0)
#     (A,valA) = opt(E,i+1,c,memo) # don't include E[i]
#     (B,valB) = opt(E,i+1, c-E[i].s,memo) # include E[i]
#     B.add(E[i])
#     valB += E[i].s
#     if valB > c: # If it exceeds capacity, then no go.
#         valB = 0
#         B = set()
#     if (valA < valB):
#         memo[(i,c)] = (B, valB)
#         return (B, valB)
#     else:
#         memo[(i,c)] = (A, valA)
#         return (A, valA)

def opt(E):
    #Helper function to prevent global memoization
    def optHelper(i,w,memo):
        # Base case
        if i < 0:
            memo[(i,w)] = (set(),0)
            return memo[(i,w)]
        # Check memo
        if (i,w) in memo:
            return memo[(i,w)]

        # New item is more than the current weight limit
        if E[i].s > w:
            output = optHelper(i-1,w,memo)
            memo[(i,w)] = output
            return output

        else:
            # Recursively call subproblem as if we include the ith element
            includeSet, includeValue = optHelper(i-1,w-E[i].s,memo)
            includeSet.add(E[i])
            includeValue += E[i].v
            # Recursively call subproblem as if we exclude the ith element
            excludeSet, excludeValue = optHelper(i-1,w,memo)

            if includeValue > excludeValue:
                output = (includeSet,includeValue)
            else:
                output = (excludeSet,excludeValue)

                memo[(i,w)] = output
            return output

    n = len(E)-1
    W = 1
    memo = {}
    output = optHelper(n,W,memo)
    return output
