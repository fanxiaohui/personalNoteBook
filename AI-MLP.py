# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 16:51:48 2018

@author: lianzeng
"""

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


def plotLine(slope, bias):
    x = np.arange(-3,3,0.5)
    y = x*slope + bias
    plt.plot(x,y)


def plotFigure(data, dataLabel, title):
    for index, label in enumerate(dataLabel):
        if label == 1:
            plt.scatter(data[index,0],data[index,1],color='red',marker='o',label='setosa')
        else:
            plt.scatter(data[index,0],data[index,1],color='blue',marker='x',label='versicolor')
    plt.xlabel('petal len')            
    plt.ylabel('sepal len')
    plt.title(title)
   
    

if __name__ == '__main__':
    data = pd.read_csv('iris.data')
    feature=data.iloc[1:len(data.index), [0,2] ].values #use two feature
    labels =data.iloc[1:len(data.index),4].values
    labels = np.where(labels=='Iris-setosa',1,-1) #because activeFunction = tanh()
    scaler = preprocessing.StandardScaler().fit(feature)
    feature_standard = scaler.transform(feature) #normalization
    
    plotFigure(feature_standard, labels,'all data')
    plt.show()
    
    
    feature_train,feature_test,label_train,label_test = train_test_split(feature_standard,labels,test_size=0.33)
    label_train = label_train.reshape(len(label_train),1)
    
    X = tf.placeholder(tf.float32, shape=[None,2])
    Y = tf.placeholder(tf.float32, shape=[None,1])
    
    W = tf.Variable(tf.random_normal([2,1],stddev=0.01))
    b = tf.Variable(tf.zeros([1,1]))
    
    H = tf.tanh(tf.matmul(X,W) + b)
    cost = tf.reduce_mean(tf.square(H - Y))
    
    train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    
    with tf.Session() as sess:        
        sess.run(tf.global_variables_initializer())
        
        for i in range(300):
            _, cost_value = sess.run([train,cost], feed_dict={X: feature_train, Y: label_train})
        
        print("costValue = %d" % cost_value)
        w1 = sess.run(W).flatten()[0]
        w2 = sess.run(W).flatten()[1]
        b = sess.run(b).flatten()[0]
        
        
        plotFigure(feature_test, label_test,'test data')
        
        #print(-w1/w2, -b/w2)        
        plotLine(-w1/w2, -b/w2)
        plt.show()
    
    print("MLP ok.")
