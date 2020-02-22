import Numberimporter
import matplotlib.pyplot as plt
import time
import random
from heapq import heappop, heappush
# Numbers to be sorted
n = 1000
# Creates an array with distinct n numbers in the range of 1 to n nonsorted
mydata = random.sample(range(n), n)


def heapsort(list):
    start = time.time()
    heap = []
    for i in list:
        heappush(heap, i)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered, time.time()-start


sorted, time = heapsort(mydata)
print(sorted)
print(time)
