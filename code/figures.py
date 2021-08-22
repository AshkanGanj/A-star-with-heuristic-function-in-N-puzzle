# importing package
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import ast

def readData(file):
    x=y = []
    with open(file) as f:
        lines = f.readlines()
        for item in lines:
            item = ast.literal_eval(item)
            x.append(item['distance'])
            y.append(item['count'])
    return x,y

plt.style.use('seaborn')
# create data
df = pd.DataFrame([['Expanded', 140, 92, 61], ['Generated', 327, 216, 148]],
                  columns=['Results', 'Misplaced', 'Manhattan', 'new_method'])
# view data
ax = df.plot(x='Results',
             kind='bar',
             stacked=False,
             title='Results')

plt.show()
x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []


x1,y1 = readData('../data1.txt')
x2,y2 = readData('../data2.txt')
x3,y3 = readData('../data3.txt')

markerline, stemlines, baseline = plt.stem(x1, y1, linefmt='darkgreen', label="misplace")
markerline.set_markerfacecolor('darkgreen')
markerline.set_markerfacecolor('none')
markerline, stemlines, baseline = plt.stem(x2, y2, linefmt='salmon', label="Manhattan")
markerline.set_markerfacecolor('salmon')
markerline.set_markerfacecolor('none')
markerline, stemlines, baseline = plt.stem(x3, y3, label="new method")
markerline.set_markerfacecolor('none')
plt.xlabel('distance')
plt.ylabel('frequency')
plt.title("states Frequency")
plt.legend()