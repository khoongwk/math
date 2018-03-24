'''
An implementation of the Gauss-Legendre
Algorithm to approximate pi. Results show
very fast convergenceto pi, with the
first 15 decimals approximated by the 4th
iteration. Significantly faster than the
Leibniz method.
'''

import math
a = 1.0
b = 1/math.sqrt(2)
t = 0.25
p = 1.0
n = 1

while n <= 8:
    result = ((a+b)**2)/(4*t)
    print('Iteration {} {}'.format(n,result))
    atemp = (a+b)/2
    btemp = math.sqrt(a*b)
    ttemp = t - p*((a-atemp)**2)
    ptemp = 2*p
    a = atemp
    b = btemp
    t = ttemp
    p = ptemp
    n+=1

print('Actual value of pi: ' + str(math.pi))

    
