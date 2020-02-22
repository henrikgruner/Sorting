
import Numberimporter
import matplotlib.pyplot as plt
import time
import random
# List with 1000000 distinct numbers from value 1-1000 randomly sorted
mydata = random.sample(range(1000), 1000)


def selectionsort(list):
    start = time.time()
    for i in range(0, len(list)):
        tempmin = i
        for j in range(i+1, len(list)):
            if list[j] < list[tempmin]:
                tempmin = j

        list[i], list[tempmin] = list[tempmin], list[i]

    return list, time.time() - start


sorted, time = selectionsort(mydata)
print(sorted)
print(time)
