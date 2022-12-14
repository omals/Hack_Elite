# -*- coding: utf-8 -*-
"""hackcsv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zeb0mCu8MrHreKcQ9xzoXs6MlK_O2fmm
"""

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

with open("bank.csv","r") as i:
  rawdata = list(csv.reader(i,delimiter = ","))

bank = np.array(rawdata[1:])
xdata = bank[:,0]
ydata = bank[:,1]

plt.figure(1,dpi=200)
plt.plot(xdata,ydata,label="xyz")