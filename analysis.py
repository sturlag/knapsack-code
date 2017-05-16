from knapsack import twobins,algorithm_A,Element
from knapsack_opt import opt,iteropt
from knapsack_det import iwama_taketomi
from knapsack_weighted import algorithm_B
import numpy
import math
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
    # Worst Case
    # values = [0.0,0.5,0.7,0.5]
    # Case b in paper
    # values = [0,0.4,0.61,0.4]
    # Random case
    values = numpy.random.rand(11)*0.4+0.3
    values[0] = 0.0
    # values = []

    elements = [Element(x,x) for x in values]
    n = len(elements)

    gen = list(algorithm_A(elements))
    gen_opt = list(iteropt(elements))

    A1 = numpy.array(map(lambda x:x[0],gen))
    print A1
    A2 = numpy.array(map(lambda x:x[1],gen))
    print A2
    avg = 0.5*(A1 + A2)
    print avg
    opt = 0.7*numpy.array(gen_opt)
    print opt

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.plot(range(n),A1,linewidth=4.0,label=r'$s(A_1)$')
    ax1.plot(range(n),A2,linewidth=4.0,label=r'$s(A_2)$')
    ax1.plot(range(n),avg,linewidth=4.0,label=r'$\frac{1}{2}\left(s(A_1)+s(A_2)\right)$',linestyle='--')
    ax1.plot(range(n),opt,linewidth=4.0,label=r'$\frac{7}{10}\cdot OPT$')
    ax1.legend(loc='lower right',fontsize=20)
    ax1.set_xticks(numpy.arange(n))
    ax2.set_xticks(numpy.arange(n))
    fig.canvas.draw()

    itemlabels = range(0,n)
    sizelabels = ['%.2f'%value for value in values]
    sizelabels[0] = ''
    ax1.set_xticklabels(itemlabels,fontsize=20)
    ax1.tick_params(axis='y',labelsize=20)
    ax1.set_ylabel('Value',fontsize=30)
    ax1.set_xlabel('Time Step',fontsize=30)

    ax2.plot(range(n),numpy.ones(n))
    ax2.set_xticklabels(sizelabels,fontsize=20)
    ax2.set_xlabel('Item Sizes',fontsize=20)

    fig.canvas.draw()
    plt.show()

def plotTwoBins():
    # Random inputs
    # values = numpy.random.rand(11)*0.3+0.1
    # values[0] = 0.0

    # Bin1 and Bin2 values cross
    # values = [0.0,0.3,0.1,0.2,0.1,0.4,0.4,0.2,0.4,0.3,0.3]

    # Worst Case
    values = [0.0,0.51,0.5,1.0]

    elements = [Element(x,x) for x in values]
    n = len(elements)

    gen = list(twobins(elements))
    gen_opt = list(iteropt(elements))

    bin1 = numpy.array(map(lambda x:x[0],gen))
    bin2 = numpy.array(map(lambda x:x[1],gen))
    avg = 0.5*(bin1+bin2)
    opt = 0.5*numpy.array(gen_opt)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.plot(range(n),bin1,linewidth=4.0,label=r'$s(B_1)$')
    ax1.plot(range(n),bin2,linewidth=4.0,label=r'$s(B_2)$')
    ax1.plot(range(n),avg,linewidth=4.0,label=r'$\frac{1}{2}\left(s(B_1)+s(B_2)\right)$',linestyle='--')
    ax1.plot(range(n),opt,linewidth=4.0,label=r'$\frac{1}{2}\cdot OPT$')
    ax1.legend(loc='upper left',fontsize=20)
    ax1.set_xticks(numpy.arange(n))
    ax2.set_xticks(numpy.arange(n))
    fig.canvas.draw()

    itemlabels = range(n)
    sizelabels = ['%.2f'%value for value in values]
    sizelabels[0] = ''
    ax1.set_xticklabels(itemlabels,fontsize=20)
    ax1.tick_params(axis='y',labelsize=20)
    ax1.set_ylabel('Value',fontsize=30)
    ax1.set_xlabel('Time Step',fontsize=30)

    ax2.plot(range(n),numpy.ones(n))
    ax2.set_xticklabels(sizelabels,fontsize=20)
    ax2.set_xlabel('Item Sizes',fontsize=30)
    # plt.subplots_adjust(left=0.7,bottom=0.14,)
    plt.show()

def plotAlgorithB():
    #Random
    # sizes = numpy.random.rand(10)*0.5
    # values = numpy.random.rand(10)*0.2
    # values[0] = 0.0

    #Max wins
    # sizes = [1.0,0.2,0.1,1]
    # values = [0.0,0.1,0.3,0.8]

    #Worst case
    epsilon = 0.1
    m = int(math.ceil(round(3/epsilon)))
    sizes = [1,1,0.5+1./(2*m)]+[1./(2*m)]*m
    values = [0,1,1-2./m]+[1./m]*m
    print sizes
    print values
    elements = [Element(sizes[i],values[i]) for i in range(len(sizes))]
    n = len(elements)

    gen = list(algorithm_B(elements))
    gen_opt = list(iteropt(elements))

    _max = numpy.array(map(lambda x:x[0],gen))
    greedy = numpy.array(map(lambda x:x[1],gen))
    avg = 0.5*(_max+greedy)
    opt = 0.5*numpy.array(gen_opt)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.plot(range(n),_max,linewidth=4.0,label=r'$s(Max(T_i))$')
    ax1.plot(range(n),greedy,linewidth=4.0,label=r'$s(Greedy(T_i))$')
    ax1.plot(range(n),avg,linewidth=4.0,label=r'$\frac{1}{2}\left(s(Max(T_i))+s(Greedy(T_i))\right)$',linestyle='--')
    ax1.plot(range(n),opt,linewidth=4.0,label=r'$\frac{1}{2}\cdot OPT$')
    ax1.legend(loc='upper left',fontsize=20)
    ax1.set_xticks(numpy.arange(n))
    ax2.set_xticks(numpy.arange(n))
    fig.canvas.draw()

    itemlabels = range(n)
    sizelabels = ['(%.2f,%.2f)'%(sizes[i],values[i]) for i in range(len(sizes))]
    sizelabels[0] = ''
    ax1.set_xticklabels(itemlabels,fontsize=20)
    ax1.tick_params(axis='y',labelsize=20)
    ax1.set_ylabel('Value',fontsize=30)
    ax1.set_xlabel('Time Step',fontsize=30)

    # ax2.plot(range(n),numpy.ones(n))
    # ax2.set_xticklabels(sizelabels,fontsize=15)
    # ax2.set_xlabel('Items (size,value)',fontsize=30)
    plt.show()

if __name__ == '__main__':
    # main()
    # worstCaseTwoBins()
    # worstCaseIwamaTaketomi()
    # plotAlgorithA()
    # plotTwoBins()
    plotAlgorithB()
