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
    B1,B2,B1_val,B2_val = algorithm_A(elements)

    return optimumValue, twobinsValue, B1,B2,B1_val,B2_val

def main():
    testsize = 10
    tests = 20

    for i in range(tests):
        print '-------------- Test ' + str(i) + ' ----------------'
        optimumValue, twobinsValue, B1, B2, B1_val, B2_val = randomTest(testsize)
        twobins_ratio = twobinsValue/optimumValue
        print 'Optimum: ' + str(optimumValue)
        print 'Twobins: ' + str(twobinsValue)
        print 'Twobins Ratio: ' + str(twobins_ratio)
        print
        print 'B1:', [str(element) for element in B1]
        print 'Value:', B1_val
        print 'B2:', [str(element) for element in B2]
        print 'Value:', B2_val
        print 'Average:', (B1_val + B2_val)*0.5
        print 'Average Ratio:', (B1_val + B2_val)*0.5/optimumValue

def worstCaseTwoBins():
    epsilon = 1e-10
    elements = [Element(x,x) for x in [0.5+epsilon,0.5+epsilon,1.,1.,1.]]
    optimumValue = opt(elements)[1]
    twobinsValue = twobins(elements)[1]
    ratio = twobinsValue/optimumValue

    print('------------------ Two Bins Worst Case -----------------')
    print('Optimum: ' + str(optimumValue))
    print('Twobins: ' + str(twobinsValue))
    print('Ratio:   ' + str(ratio))

if __name__ == '__main__':
    main()
    worstCaseTwoBins()
