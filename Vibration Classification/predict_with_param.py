# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:33:04 2018

@author: namta
"""
from __future__ import print_function
import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

def main():
    with open('input.pkl', 'rb') as fin:
        saved_param = pickle.load(fin)
    
    # Change String in Pickle to Float
    f_param = []
    for j in range(len(saved_param)):
        f_param.append([float(i) for i in saved_param[j]])
    
    key = []
    value = []
    print("Input data : {}".format(len(f_param)))
    
    for v in range(len(f_param)):
    #for v in range(151):
        key.append(f_param[v][0])
        value.append(f_param[v][1:])
    
    key = np.asarray(key)
    value = np.asarray(value)
    
    #print(key)
    #print(value)
    
    # Change list to Dictionary
    dataset = {}
    dataset['label'] = key
    dataset['data'] = value
    #print(dataset.keys())
    #print(dataset)
    
    X_Dataset = dataset['data']
    y_Dataset = dataset['label']
    #print(X_Dataset.shape)
    #print(y_Dataset.shape)
    #print(y_Dataset)
    
####################################################################################################################################################################
####################################################################################################################################################################
    
    np.random.seed(0)
    indices = np.random.permutation(len(X_Dataset))
    #print(X_Dataset.shape)
    x_train = X_Dataset[indices[:-1]]
    y_train = y_Dataset[indices[:-1]]
    x_test = X_Dataset[indices[-1:]]
    y_test = y_Dataset[indices[-1:]]
    
    print("x_train    : {}".format(x_train.shape))
    print("y_train    : {}".format(y_train.shape))
    print("x_test     : {}".format(x_test.shape))
    print("y_test     : {}".format(y_test.shape))
    
    with open('learned param.dat', 'rb') as fin:
        knn = pickle.load(fin)
        
    knn.fit(x_train, y_train)
    kX = knn.predict(x_test)
    
    print(kX)
    #print("test result: {:.2f}".format(knn.score(x_test, y_test)))
    
    return kX
    
