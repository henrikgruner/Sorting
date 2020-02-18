import scipy.fftpack
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import scipy
import pandas as pd
import time

import csv
import Numberimporter
import unicodecsv

mydata = Numberimporter.NUMBERS

# bubble sort?


def insertionsort(list):
    start_time = time.time()

    for i in range(1, len(list)):
        item = list[i]
        j = i-1
        while j > 0 and item < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = item

    end_time = time.time() - start_time
    return list, end_time


plt.plot(mydata)

lol = insertionsort(mydata)
plt.plot(lol[0])
plt.title(lol[1])
plt.show()
