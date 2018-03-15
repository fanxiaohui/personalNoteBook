# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:23:33 2018

@author: lianzeng
"""

#data from  https://github.com/caicloud/tensorflow-tutorial/tree/master/Deep_Learning_with_TensorFlow/datasets/MNIST_data


import struct
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#data format refer to:  http://yann.lecun.com/exdb/mnist/
IMAGE_FILE_HEADER_SIZE = 16 
LABEL_FILE_HEADER_SIZE = 8
LABEL_NUM = 10

training_epochs = 20
batch_size = 100

def imshow(img, size):
    img = img.reshape(size)    
    plt.imshow(img)
    plt.show()

def readImag(filename):        
    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(IMAGE_FILE_HEADER_SIZE))
        img = np.fromfile(f, dtype=np.uint8).reshape(num, rows*cols)
        #imshow(img[0],[rows,cols])
        return img
        

def readLable(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(LABEL_FILE_HEADER_SIZE))
        labels = np.fromfile(f, dtype=np.uint8) #labels[0] = 7   
        
    return convertLable(labels)    
        

def convertLable(labels):
    mnistlabel = np.zeros(shape = (len(labels),LABEL_NUM), dtype = np.uint8)
    for i in range(len(labels)):
        mnistlabel[i][labels[i]] = 1
    print(mnistlabel[0])
    print(mnistlabel[1])    
    return mnistlabel        

def getBatch(data,label,batchIndex,batchSize):
    xs = data[batchIndex*batchSize : (batchIndex + 1)*batchSize]
    ys = label[batchIndex*batchSize : (batchIndex + 1)*batchSize]
    assert(xs.shape == (batchSize,784) )
    assert(ys.shape == (batchSize,LABEL_NUM) )    
    print(ys[0])
    return (xs,ys)


X = tf.placeholder(tf.float32, shape = [None,784]) #28*28 = 784, image size
Y = tf.placeholder(tf.float32, shape = [None,LABEL_NUM])
W = tf.Variable(tf.random_normal([784, LABEL_NUM]))
b = tf.Variable(tf.random_normal([LABEL_NUM]))

#H = tf.nn.softmax(tf.matmul(X,W) + b)
#cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(H), axis = 1))
#optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01).minimize(cost)
H = tf.matmul(X,W) + b
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = H, labels = Y))
optimizer = tf.train.AdamOptimizer(learning_rate = 0.01).minimize(cost)

correct_prediction = tf.equal(tf.argmax(H, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

if __name__ == '__main__':
    trainImg = readImag('./MNistData/train-images.idx3-ubyte') #shape=(10000,784)
    trainLabels = readLable('./MNistData/train-labels.idx1-ubyte')
    testImg = readImag('./MNistData/t10k-images.idx3-ubyte') #shape=(10000,784)
    testLabels = readLable('./MNistData/t10k-labels.idx1-ubyte')
    numExamples = trainImg.shape[0]
    assert(numExamples == 60000)
    
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(training_epochs):
            avg_cost = 0
            batchNum = numExamples//batch_size
            assert(batchNum == 600)
            for i in range(batchNum):
                batch_xs, batch_ys = getBatch(trainImg,trainLabels,i,batch_size)
                c,_ = sess.run([cost,optimizer],feed_dict = {X:batch_xs, Y:batch_ys})
                avg_cost += c/batchNum
                
            print('Epoch:','%04d' %(epoch+1), 'cost = ','{:.9f}'.format(avg_cost))
            
        print('Learning Finished!')    
        print("Accuracy: ", sess.run(accuracy, feed_dict = {X:testImg, Y:testLabels}) )        
    
    
            
 
 
