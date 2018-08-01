'''
Euclidian algorithm - a method to calculate the greatest common divisor between two natural numbers.
With two of such numbers, a and b, the following are the steps:
a % b = c, where c is the remainder.
Repeat with a = b and b = c:
b % c = d ... and so on until d = 0, and c will be the greatest common divisor.

e.g a = 1053, b = 541
1053 % 541 = 512
541 % 512 = 29
512 % 29 = 19
29 % 19 = 10
19 % 10 = 9
10 % 9 = 1
9 % 1 = 0 hence 1 is the greatest common divisor.

Going to make an recursive implementation of this algorithm.
'''

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
def gcd(x, y):
    temporary = x % y
    print('{} % {} = {}'.format(x,y,temporary))

    if x % y == 0:
        print('Greatest common divisor is ', y)
        return
    else:
        gcd(y, temporary)

gcd(a,b)
