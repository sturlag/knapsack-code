from knapsack import twobins,algorithm_A,Element
from knapsack_opt import opt,iteropt
from knapsack_det import iwama_taketomi
from knapsack_weighted import algorithm_B
import numpy
import matplotlib.pyplot as plt


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
    detValue = iwama_taketomi(elements)[1]
    B1,B2,B1_val,B2_val = algorithm_A(elements)

    return optimumValue, twobinsValue, B1,B2,B1_val,B2_val, detValue

def main():
    testsize = 10
    tests = 20

    for i in range(tests):
        print '-------------- Test ' + str(i) + ' ----------------'
        optimumValue, twobinsValue, B1, B2, B1_val, B2_val, detValue = randomTest(testsize)
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
        print
        print 'Iwama Taketomi:', detValue
        print 'Iwama Taketomi Ratio:', detValue/optimumValue

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

def worstCaseIwamaTaketomi():
    t = (numpy.sqrt(5)-1)/2.0
    epsilon = 1e-5
    e1 = t+epsilon
    e2 = 1 - t
    e3 = t

    elements = [Element(x,x) for x in [e1,e2,e3]]

    optimumValue = opt(elements)[1]
    det,detValue = iwama_taketomi(elements)
    B1,B2,B1_val,B2_val = algorithm_A(elements)
    B_val = 0.5*(B1_val + B2_val)
    ratio = detValue/optimumValue
    ratio_A = B_val/optimumValue

    print('------------------ Iwama Taketomi Worst Case -----------------')
    print('Optimum: ' + str(optimumValue))
    print('Iwama Taketomi: ' + str(detValue))
    print('Ratio:   ' + str(ratio))
    print('Algorithm A Ratio: ' + str(ratio_A))

def plotAlgorithA():
    n = 20
    values = numpy.random.rand(n)*0.5
    elements = [Element(x,x) for x in values]

    gen = list(algorithm_A(elements))
    gen_opt = list(iteropt(elements))

    X = numpy.zeros((4,n))
    X[0,:] = numpy.array(map(lambda x:x[0],gen))
    X[1,:] = numpy.array(map(lambda x:x[1],gen))
    X[2,:] = 0.5*(X[0,:] + X[1,:])
    X[3,:] = 0.7*numpy.array(gen_opt)

    X = X.transpose()

    plt.plot(X)
    plt.legend(['A1','A2','AVG','0.7 OPT'])
    plt.show()

def plotTwoBins():
    n = 10
    # values = numpy.random.rand(n)*0.2
    values = [0.3,0.1,0.2,0.1,0.4,0.4,0.2,0.4,0.3,0.3]
    elements = [Element(x,x) for x in values]

    gen = list(twobins(elements))
    gen_opt = list(iteropt(elements))

    X = numpy.zeros((3,n))
    bin1 = numpy.array(map(lambda x:x[0],gen))
    bin2 = numpy.array(map(lambda x:x[1],gen))
    avg = 0.5*(bin1+bin2)
    opt = 0.5*numpy.array(gen_opt)

    plt.plot(bin1,linewidth=4.0,label='Bin 1')
    plt.plot(bin2,linewidth=4.0,label='Bin 2')
    plt.plot(avg,linewidth=4.0,label='Average')
    plt.plot(opt,linewidth=4.0,label=r'$\frac{1}{2}\cdot OPT$',linestyle='--')
    plt.legend(loc='upper left',fontsize=20)

    xticklabels = [str(i)+'\n'+str(values[i]) for i in range(n)]
    print xticklabels
    plt.xticks(range(0,n),xticklabels,fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylabel('Knapsack Value',fontsize=30)
    plt.xlabel('Element Sizes',fontsize=30)
    plt.show()

def plotAlgorithB():
    n = 20
    values = numpy.random.rand(n)*0.2
    elements = [Element(x,x) for x in values]

    gen = list(algorithm_B(elements))
    gen_opt = list(iteropt(elements))

    X = numpy.zeros((4,n))
    X[0,:] = numpy.array(map(lambda x:x[0],gen))
    X[1,:] = numpy.array(map(lambda x:x[1],gen))
    X[2,:] = 0.5*(X[0,:] + X[1,:])
    X[3,:] = 0.5*numpy.array(gen_opt)

    print X
    X = X.transpose()
    plt.plot(X)
    plt.legend(['Max','Greedy','AVG','0.5 OPT'],loc='lower right')
    plt.show()

if __name__ == '__main__':
    # main()
    # worstCaseTwoBins()
    # worstCaseIwamaTaketomi()
    # plotAlgorithA()
    plotTwoBins()
    # plotAlgorithB()
