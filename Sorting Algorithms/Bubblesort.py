import Numberimporter
import matplotlib.pyplot as plt
import time
# List with 1000 distinct numbers from value 1-1000 randomly sorted
mydata = Numberimporter.NUMBERS


def bubblesort(list):
    start = time.time()
    n = len(list)
    for i in range(0, n):
        for j in range(0, n-1):
            if list[j+1] < list[j]:
                list[j], list[j+1] = list[j+1], list[j]
    end = time.time() - start
    return list, end


plt.plot(mydata)
lol = bubblesort(mydata)
plt.plot(lol[0])


plt.title('Bubblesort: ' + str(round(lol[1], 5)) + ' Seconds')
plt.show()
