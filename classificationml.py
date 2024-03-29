# -*- coding: utf-8 -*-

import tensorflow as tf
print(tf.__version__)

from sklearn.datasets import load_breast_cancer

data=load_breast_cancer()

data.keys()

data.data.shape

data.target.shape

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(data.data,data.target,test_size=.33)
N, D=X_train.shape

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model=tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(D,)),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

r=model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=50)

print("Train Scaore:",model.evaluate(X_train,Y_train))
print("Test Score:",model.evaluate(X_test,Y_test))

import matplotlib.pyplot as plt
plt.plot(r.history['loss'],label='loss')
plt.plot(r.history['val_loss'],label='val_loss')
plt.legend()

plt.plot(r.history['accuracy'],label='acc')
plt.plot(r.history['val_accuracy'],label='val_acc')
plt.legend()
