'''
Collatz conjecture - A conjecture with 2 rules proposed:
1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.
The conjecture states for any positive integer, the final result following these steps will always be 1.

I learnt how to use matplotlib and numpy to generate a scatter diagram of the number of steps taken to reach
1 for the first 10000 positive integers.
'''
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# x1 = int(input('Enter the number to test: ')) This line is for user testing.

def collatz(n,steps):
    current_steps = steps
    # print(n) To visualise the calculations.
    if n == 1:
        # print('Solved in', current_steps, 'steps.')
        return current_steps
    elif n % 2 == 0:
        current_steps += 1
        return collatz(n/2, current_steps)
    else:
        current_steps += 1
        return collatz(3*n + 1, current_steps)
# result = collatz(x1, 0)

# result initially returned a None object because I forgot the return in lines 18 and 21. Without the return
# the result after the final recursion wouldn't 'return' back up to the first call of collatz().

#Attempt to plot number of steps in the collatz conjecture for the first 100 integers.
x = np.linspace(1, 10000, 10000) # Creates an list of 10000 objects evenly spaced between 1 and 10000.
y = []
for i in range(1, 10001):
    y.append(collatz(i, 0)) # Creates similar list for number of steps for each x value.
plt.plot(x, y, '.', markersize=4 ,color='black') # Plots the diagram with x and y values.
plt.xlabel('n')
plt.ylabel('Steps')
plt.title('Collatz Conjecture from 1 to 10000')
plt.show() # Shows plot.
