'''
Approximation of the golden ratio
using the fibonacci series (1, 1,
2, 3, 5, 8, 13,...) For the terms
T1, T2,... Tn, the general
formula for the term Tn+2 =
Tn+1 + Tn. If we divide Tn+1/Tn,
the result will approach the
golden ratio 1.618033... as n
increases from 1 towards 
infinity, as shown from
the following code. The
approximation is reasonably
accurate by the 41th term, at 
15 decimal points of precision.
'''
from __future__ import division
def fibonacci(n):
    # n is the number of terms
    # to display.
    current = 1 #initialise the first two terms.
    next = 1
    print(current)
    print(next)
    temp = 0
    count = 3
    while count <= n:
        temp = current + next
        current = next
        next = temp
        ratio = next/current
        print('Iteration {}: {} Ratio: {}'.format(count,next,ratio))
        count += 1
fibonacci(50)

'''
Interestingly, this observation
is not unique to the fibonacci
series. It turns out that Tn+1/Tn
-> 1.618033... as long as T1+T2
are not both zero. Negative numbers
and decimal inputs work fine.
'''
def generalSeries(n):
    # n is the number of terms
    # to display.
    current = float(input('Input first term: '))
    #initialise the first two terms.
    next = float(input('Input second term: '))
    print ('\n')
    print('Iteration 1: {}'.format(current))
    print('Iteration 2: {} Ratio {}'.format(next, next/current))
    temp = 0
    count = 3
    while count <= n:
        temp = current + next
        current = next
        next = temp
        ratio = next/current
        print('Iteration {}: {} Ratio: {}'.format(  count,next,ratio))
        #print(str(next) + ' Ratio ' + str(ratio))
        count += 1

generalSeries(50)
