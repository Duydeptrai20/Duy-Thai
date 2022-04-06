import tensorflow as tf
from tensorflow.python import keras
from keras import datasets
import cv2
#data 2: shuffled and split between train and test sets
(X_train, y_train),(X_test,y_test)= datasets.mnist.load_data()
sample=X_train[1000]
cv2.imshow('ChuSo',sample)
label=y_train[500]
print(label)
cv2.waitKey(0)
