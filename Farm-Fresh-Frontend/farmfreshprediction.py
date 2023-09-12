# -*- coding: utf-8 -*-
"""FarmFreshPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H9hT5fjDGCYk9MLCguUJ8UoeE-R7QcBV

import libs
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from pandas import read_csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import LinearSVR, SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import warnings
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense,Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import array as arr
import joblib

"""importing data

"""

data = read_csv('Vegetable_market.csv')

"""app

"""

app = Flask(__name__,template_folder='project_updated\project\templates\in.html')

"""preprocessing

"""

def preprocess_inp(data):
    data = data.copy()

    data['Vegetable'] = data['Vegetable'].replace({
        'cabage': 1,
        'radish': 2,
        'potato': 3,
        'tomato ': 4,
        'peas': 5,
        'pumkin': 6,
        'cucumber': 7,
        'pointed grourd ': 8,
        'Raddish': 9,
        'Bitter gourd': 10,
        'onion': 11,
        'ginger': 12,
        'garlic': 13,
        'califlower': 14,
        'brinjal': 15,
        'okra': 16,
        'chilly': 17,
    })

    data['Deasaster Happen in last 3month'] = data['Deasaster Happen in last 3month'].replace({'no' : 0,'yes' : 1})

    data['Month'] = data['Month'].replace({
        'jan' : 1,
        'feb':2 ,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6 ,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec' : 12,
        ' ' : np.NaN
    })

    data['Month'] = data['Month'].fillna(data['Month'].mode()[0])

    data['Vegetable condition'] = data['Vegetable condition'].replace({'fresh' : 0,'avarage':1,'scrap':2})

    data['Season'] = data['Season'].replace({'winter' : 0,'summer':1,'spring':2,'autumn': 3,'monsoon':4})

    return data

input = preprocess_inp(data)

y = input['Price per kg'].values
X = input.drop(['Price per kg'],axis=1).values

X

y

X_train , X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,shuffle=False)

y_test

"""Training"""

model = Sequential()
model.add(LSTM(50,input_shape=(X_train.shape[1],1)))
model.add(Dense(units=1))

model.summary()

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(X_train,y_train,epochs=100,batch_size=32,verbose=1)

# from google.colab import drive
# drive.mount('/content/drive')

trainpred = model.predict(X_train)
testpred = model.predict(X_test)

trainrmse = np.sqrt(mean_squared_error(y_train,trainpred))
testrmse = np.sqrt(mean_squared_error(y_test,testpred))
print('Train RMSE: ', trainrmse)
print('Test RMSE: ', testrmse)

# joblib.dump(model, "/content/drive/MyDrive/model2/model.sav")
with open('C:/Users/Piyush/Desktop/Git Uploads/Farm-Fresh/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

import matplotlib.pyplot as plt

# Plot actual vs. predicted prices
plt.figure(figsize=(12, 6))

# Plot training data
plt.subplot(2, 1, 1)
plt.plot(y_train, label='Actual Prices')
plt.plot(trainpred, label='Predicted Prices')
plt.title('Training Data: Actual vs. Predicted Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

# Plot testing data
plt.subplot(2, 1, 2)
plt.plot(y_test, label='Actual Prices')
plt.plot(testpred, label='Predicted Prices')
plt.title('Testing Data: Actual vs. Predicted Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()

plt.tight_layout()
plt.show()

"""input check"""

# inp = pd.read_csv('new.csv')

# veg  = inp['Vegetable']

# inpt = preprocess_inp(inp)

# predicted_price = model.predict(inpt)

# for i in range (0,15):
#     print("For : ",veg[i] ," - " ,"Predicted Price :", predicted_price[i][0])



@app.route('/', methods=['POST','GET'])
def predict():
    #variables
    
    inp = pd.read_csv('new.csv')

    veg  = inp['Vegetable']
    selected_vegetable = request.form.get('Vegetable')
    inpt = preprocess_inp(inp)

    predicted_price = model.predict(inpt)
    output = 'The price of'+ selected_vegetable+'  will be Rs. ' + \
        str(predicted_price) + ' in future.'
    return jsonify({"output":output})



if __name__ == '__main__':
    app.run(debug=True)
