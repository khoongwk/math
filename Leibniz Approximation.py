'''
Demonstrating the Leibniz
algorithm, which states that
1 - 1/3 + 1/5 - 1/7 + ...= pi/4.
My experimentation with this
algorithm shows that it is
very slow. Even after summing
and subtracting 5000 of the
above numbers in the series,
the approximation is only
accurate to 3 decimal places.
'''
import math
def piAlgorithm():
    sum = 0.0
    count = 1.0
    toAdd = True
    while count <= 10000:
        if toAdd is True:
            sum += 1/count
            toAdd = False
        elif toAdd is False:
            sum -= 1/count
            toAdd = True
        count += 2
        print(sum*4)
    print('Approximation: {} in {} iterations'.format(sum*4, math.floor(count/2)))
    print ('Actual Value: '+ str(math.pi))
piAlgorithm()
