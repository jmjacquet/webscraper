# from collections import Counter

# counter = Counter(['a', 'a', 'b'])
# print(counter)


import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]

y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()