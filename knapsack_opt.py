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
            includeSet.add(str(E[i]))
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
