import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import datasets
import cv2

#data: shuffled and split between train and test sets
(X_train, y_train), (X_test,y_test)= datasets.mnist.load_data()

sample= X_test[100]
cv2.imshow('Digit', sample)
#reshape
X_train = X_train.reshape((6000, 28, 28,1))
X_test = X_test.reshape((10000, 28, 28,1))
#normalize
X_train, X_test = X_train/255.0, X_test/ 255.0

# cast
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

model_architecture= "digit_config.json"
model_weights = "digit_weight.h5"
model=model_from_json(open(model_architure).read())
model.load_weight(model_weights)

optim = Adam()
model.compile(loss="categorical_crossentropy",optimizer=optim,metrio)

sample