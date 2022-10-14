#!/bin/python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.preprocessing import StandardScaler




if __name__ == '__main__':
    timeCharged = float(input().strip())


df = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])

df = df[df['lasted']<8]

x_train = df[['charged']]
y_train = df['lasted']


model = Ridge()
model.fit(x_train,y_train)

pred  = model.predict([[timeCharged]])

if pred[0] > 8:
    print(8.0)
else:
    print(round(timeCharged*2,2))



