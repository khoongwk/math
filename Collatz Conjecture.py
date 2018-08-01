'''
Collatz conjecture - A conjecture with 2 rules proposed:
1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.
The conjecture states for any positive integer, the final result following these steps will always be 1.
'''

x = int(input('Enter the number to test: '))

def collatz(n):
    print(n)
    if n == 1:
        print('Solved')
        return
    elif n % 2 == 0: collatz(n/2)
    else: collatz(3*n + 1)

collatz(x)