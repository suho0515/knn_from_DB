# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:00:12 2018

@author: KO
"""


import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split 
#from sklearn.neighbors import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
import pickle
#import tensorflow as tf

def main(param_pickle):
    
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    
    print(iris.keys())
    print(digits.keys())
    
    x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=30) 
    
    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)
        
    iris = datasets.load_iris()
    iris_x = iris.data
    iris_y = iris.target
    print(np.unique(iris_y))
    
    np.random.seed(0)
    indices = np.random.permutation(len(iris_x))
    iris_x_train = iris_x[indices[:-1]]
    iris_y_train = iris_y[indices[:-1]]
    iris_x_test = iris_x[indices[-1:]]
    iris_y_test = iris_y[indices[-1:]]
    
    with open(param_pickle, 'rb') as fin:
        knn = pickle.load(fin)
        
    kX = knn.predict(iris_x_test)
    print("kX:")
    print(kX.shape)
    print(kX)
    print(y_test)
    print("test result: {:.2f}".format(knn.score(x_test, y_test)))
        
    
    # Linear Model
    diabetes = datasets.load_diabetes()
    diabetes_x_train = diabetes.data[:-20]
    diabetes_x_test = diabetes.data[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_x_train, diabetes_y_train)
    print(regr.coef_)
    print(regr.intercept_)
    
    np.mean((regr.predict(diabetes_x_test)-diabetes_y_test)**2)
    rs = regr.score(diabetes_x_test, diabetes_y_test)
    print("Accuracy : {:.2f}".format(rs))

    return rs, kX[0]

main('Data_param.dat')