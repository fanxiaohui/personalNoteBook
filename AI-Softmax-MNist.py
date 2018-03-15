
"""
Created on Thu Mar 15 10:23:33 2018

@author: lianzeng
"""

#data from  https://github.com/caicloud/tensorflow-tutorial/tree/master/Deep_Learning_with_TensorFlow/datasets/MNIST_data


import struct
import numpy as np
import matplotlib.pyplot as plt


#data format refer to:  http://yann.lecun.com/exdb/mnist/
IMAGE_FILE_HEADER_SIZE = 16 
LABEL_FILE_HEADER_SIZE = 8
LABEL_NUM = 10

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

if __name__ == '__main__':
    testImg = readImag('./MNistData/t10k-images.idx3-ubyte') #shape=(10000,784)
    labels = readLable('./MNistData/t10k-labels.idx1-ubyte')
    
    
            
    
    
            
 
 
