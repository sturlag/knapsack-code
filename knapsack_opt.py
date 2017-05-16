from knapsack import Element
from fractions import *

def opt(E):
    #Helper function to prevent global memoization
    def optHelper(i,w,memo):
        # print (i,w)
        # Base case
        if i < 0:
            memo[(i,w)] = (list(),Fraction('0'))
            return memo[(i,w)]
        # Check memo
        if (i,w) in memo:
            return memo[(i,w)]

        # New item is more than the current weight limit
        if E[i].s > w:
            # print 'exclude ' + str(E[i])
            output = optHelper(i-1,w,memo)
            memo[(i,w)] = output
            return output

        else:
            # Recursively call subproblem as if we include the ith element
            # print 'include ' + str(E[i])
            includeSet, includeValue = optHelper(i-1,w-E[i].s,memo)
            includeSet.append(str(E[i]))
            includeValue += E[i].v
            # Recursively call subproblem as if we exclude the ith element
            # print 'exclude ' + str(E[i])
            excludeSet, excludeValue = optHelper(i-1,w,memo)

            if includeValue > excludeValue:
                output = (includeSet,includeValue)
            else:
                output = (excludeSet,excludeValue)

                memo[(i,w)] = output
            return output

    n = len(E)-1
    W = Fraction('1.0')
    memo = {}
    output = optHelper(n,W,memo)
    return output

def iteropt(E):
    for i in xrange(1,len(E)+1):
        yield opt(E[:i])[1]

def main():
    test = [0.2,0.61,0.4,0.4]
    elements = [Element(x,x) for x in test]
    # print [str(e) for e in elements]
    print opt(elements)

if __name__ == '__main__':
    main()
