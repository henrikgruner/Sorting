import Numberimporter
import matplotlib.pyplot as plt
import time
mydata = Numberimporter.NUMBERS

# bubble sort?


def insertionsort(list):
    start_time = time.time()
    # Iterates over the whole list
    for i in range(0, len(list)):
        j = i
        while j > 0:
            if(list[j-1] > list[j]):
                list[j], list[j-1] = list[j-1], list[j]
            j -= 1
    end_time = time.time() - start_time

    print("\n", end_time, ' Seconds')
    return list, end_time


plt.plot(mydata)

lol = insertionsort(mydata)
plt.plot(lol[0])
plt.title(lol[1])
plt.show()
