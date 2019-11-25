# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:10:31 2018

@author: namta
"""
from __future__ import print_function
import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

import mysql.connector as mariadb
from mysql.connector import Error


def read_data(cursor, table,f_param):
    sql_select_Query="select * from " + table
    cursor.execute(sql_select_Query)

    temp_param = []  # list for temporary raw data
    for row in cursor:
        # print("time_peak = ", row[3], )
        # print("time_rms = ", row[2])
        # print("crest_factor  = ", row[4])
        # print("frequency_peak  = ", row[5])
        # print("frequency_band  = ", row[11], "\n")
        # print(type(row))
        temp_param = []
        temp_param.append(table)  # label
        temp_param.append(row[3])  # time_peak
        temp_param.append(row[2])  # time_rms
        temp_param.append(row[4])  # crest_factor
        temp_param.append(row[5])  # frequency_peak
        temp_param.append(row[11])  # frequency_band
        f_param.append(temp_param)
    # cursor.close()
    print(f_param)

    return f_param


try:

    connection = mariadb.connect(host='signallinkdb.synology.me', user='signallink', port='3307', password='signa!!ink0300', database='signallink')

    if connection.is_connected():

        db_Info = connection.get_server_info()

        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

        print("Your connected to -", record)



        #sql_select_Query = "select * from data_sensor"
        #cursor.execute(sql_select_Query)

        f_param = [] # list for parameters

        f_param = read_data(cursor, "normal_data", f_param)
        f_param = read_data(cursor, "impact_data", f_param)
        f_param = read_data(cursor, "vibration_data", f_param)

        key = []
        value = []
        print("Input data : {}".format(len(f_param)))

        for v in range(len(f_param)):
            # for v in range(151):
            key.append(f_param[v][0])
            value.append(f_param[v][1:])

        key = np.asarray(key)
        value = np.asarray(value)

        # print(key)
        # print(value)

        # Change list to Dictionary
        dataset = {}
        dataset['label'] = key
        dataset['data'] = value
        # print(dataset.keys())
        # print(dataset)

        X_Dataset = dataset['data']
        y_Dataset = dataset['label']
        # print(X_Dataset.shape)
        # print(y_Dataset.shape)
        # print(y_Dataset)

        ####################################################################################################################################################################
        ####################################################################################################################################################################

        # np.random.seed(0)
        indices = np.random.permutation(len(X_Dataset))
        # print(X_Dataset.shape)

        # indices = np.arange(len(X_Dataset))
        # np.random.shuffle(indices)

        x_train = X_Dataset[indices[:-200]]
        y_train = y_Dataset[indices[:-200]]
        x_test = X_Dataset[indices[-200:]]
        y_test = y_Dataset[indices[-200:]]
        print(y_test)
        knn = KNeighborsClassifier()

        print("x_train    : {}".format(x_train.shape))
        print("y_train    : {}".format(y_train.shape))
        print("x_test     : {}".format(x_test.shape))
        print("y_test     : {}".format(y_test.shape))

        knn.fit(x_train, y_train)
        kX = knn.predict(x_test)

        print("test result: {:.2f}".format(knn.score(x_test, y_test)))

        '''
        for c in range(len(f_param)):
            if f_param[c][0] not in dataset:
                dataset[f_param[c][0]] = [f_param[c][1:]]
            else:
                dataset[f_param[c][0]].append(f_param[c][1:])
        '''
        ####################################################################################################################################################################
        ####################################################################################################################################################################
        '''
        # Pickle

        # for writing
        with open('learned param', 'wb') as fout:
            pickle.dump(InData, fout)

        # for reading
        with open('learned param', 'rb') as fin:
            saved_param = pickle.load(fin)

        print(saved_param)
        '''
        ####################################################################################################################################################################
        ####################################################################################################################################################################
        '''
        # Pandas

        index = range(0, 10, 1)
        df = pd.DataFrame(np.random.randn(10,1), index=index, columns=['bin'])
        print(df)
        #print(df.describe())
        print(df['bin'].max())
        print(df['bin'].min())
        print(df['bin'].mean())
        print(df['bin'].var())

        # for writing
        with open('learned param', 'wb') as fout:
            pickle.dump(InData, fout)
        '''
except Error as e:

    print("Error while connecting to MySQL", e)

# finally:
#    if(connection.is_connected()):
#        cursor.close()
#        connection.close()
#        print("MySQL connection is closed")



















    with open('input_ROBO.pkl', 'rb') as fin:
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

    #np.random.seed(0)
    indices = np.random.permutation(len(X_Dataset))
    #print(X_Dataset.shape)

    #indices = np.arange(len(X_Dataset))
    #np.random.shuffle(indices)



    x_train = X_Dataset[indices[:-200]]
    y_train = y_Dataset[indices[:-200]]
    x_test = X_Dataset[indices[-200:]]
    y_test = y_Dataset[indices[-200:]]
    print(y_test)
    knn = KNeighborsClassifier()

    with open('learned param_ROBO.dat', 'wb') as fout:
        pickle.dump(knn, fout)

    print("x_train    : {}".format(x_train.shape))
    print("y_train    : {}".format(y_train.shape))
    print("x_test     : {}".format(x_test.shape))
    print("y_test     : {}".format(y_test.shape))

    knn.fit(x_train, y_train)
    kX = knn.predict(x_test)

    print("test result: {:.2f}".format(knn.score(x_test, y_test)))


    '''
    for c in range(len(f_param)):
        if f_param[c][0] not in dataset:
            dataset[f_param[c][0]] = [f_param[c][1:]]
        else:
            dataset[f_param[c][0]].append(f_param[c][1:])
    '''
    ####################################################################################################################################################################
    ####################################################################################################################################################################
    '''
    # Pickle
    
    # for writing
    with open('learned param', 'wb') as fout:
        pickle.dump(InData, fout)
        
    # for reading
    with open('learned param', 'rb') as fin:
        saved_param = pickle.load(fin)
        
    print(saved_param)
    '''
    ####################################################################################################################################################################
    ####################################################################################################################################################################
    '''
    # Pandas
    
    index = range(0, 10, 1)
    df = pd.DataFrame(np.random.randn(10,1), index=index, columns=['bin'])
    print(df)
    #print(df.describe())
    print(df['bin'].max())
    print(df['bin'].min())
    print(df['bin'].mean())
    print(df['bin'].var())
    
    # for writing
    with open('learned param', 'wb') as fout:
        pickle.dump(InData, fout)
    '''