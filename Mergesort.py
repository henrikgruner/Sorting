
import Numberimporter
import matplotlib.pyplot as plt
import time

mydata = Numberimporter.NUMBERS


def mergesort(list):
    starttime = time.time()
    if len(list) > 1:

        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    end_time = time.time()-starttime
    return list, end_time


plt.plot(mydata)
sorted, time = mergesort(mydata)
print(sorted)
plt.plot(sorted)
plt.title(time)
plt.show()
print('seconds: ', time)
