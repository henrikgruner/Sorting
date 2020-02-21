import Numberimporter
import matplotlib.pyplot as plt
import time
import random

mydata = random.sample(range(1000000), 1000000)


def quicksort(list):
    if(len(list) < 2):
        return list
    pivot = list[0]
    # Recursive calls
    lesser = quicksort([i for i in list[1:] if i <= pivot])
    bigger = quicksort([i for i in list[1:] if i > pivot])

    lesser.append(pivot)
    lesser.extend(bigger)

    return lesser


plt.plot(mydata)
lol = quicksort(mydata)
plt.plot(lol)
plt.title('Quicksort')
plt.show()
