from knapsack import twobins,algorithm_A,Element
from knapsack_opt import opt
import numpy


test1 = [Element(x,x) for x in [0.3, 0.4, 0.6]]
sol1 = 1.0

test2 = [Element(x,x) for x in [0.5,0.5]]
sol2 = 1.0

test3 = [Element(x,x) for x in [0.2,0.9,0.4,0.35]]
sol3 = 0.95

def randomTest(n):
    values = numpy.random.rand(n)*0.1+0.49
    elements = [Element(x,x) for x in values]

    optimumValue = opt(elements)[1]
    twobinsValue = twobins(elements)[1]

    return optimumValue, twobinsValue

def main():
    testsize = 500
    tests = 20

    for i in range(tests):
        print '-------------- Test ' + str(i) + ' ----------------'
        optimumValue, twobinsValue = randomTest(testsize)
        ratio = twobinsValue/optimumValue
        print 'Optimum: ' + str(optimumValue)
        print 'Twobins: ' + str(twobinsValue)
        print 'Ratio: ' + str(ratio)

if __name__ == '__main__':
    main()
