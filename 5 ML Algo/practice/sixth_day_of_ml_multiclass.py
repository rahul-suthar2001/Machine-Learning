import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sns
from sklearn import metrics
# classification can also be dependent on multiple features
# images are always stored in the form of the metrices
# we have inbuilt dataset in sklearn
# digits data in sklearn
# 1797 images in 8x8 metrix
from sklearn.datasets import load_digits
digits=load_digits()
# dir() to see the func's present in the digits : it will us the list
dir(digits)
plt.gray()
for i in range(5):
    # matshow will represent the image from the digits dataset
    plt.matshow(digits.images[i])
    plt.show()
# data() func give the value of each pixel by keeping each rows of the 8x8 metrix
# side by side : it will give 1d array
print(digits.data[0])
# we will be analysing the 64 values
print(digits.target[0:5])
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
md=LogisticRegression()
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.2)
md.fit(x_train,y_train)
plt.matshow(digits.images[60])
plt.show()
print(digits.target[60])
print(md.predict([digits.data[60]]))
print(md.predict(x_test))
print(md.predict(digits.data[0:5]))
print(md.score(x_test,y_test))
# it's giving very high accuracy but for 4-5 % it is not predicting correct
# values for this we will make confusion matrix
from sklearn.metrics import confusion_matrix
y_predicted=md.predict(x_test)
cm=confusion_matrix(y_test,y_predicted)
# it will give us the matrix
# rows will us actual values
# columns are predicted values
print(cm)
plt.figure(figsize=(10,8))
sns.heatmap(cm,annot=True)
plt.xlabel("predicted values")
plt.ylabel("actual values ")
plt.show()
print("-------x-------------x------------------x------------------x-----------")
from sklearn.datasets import load_iris
dt=load_iris()
print(dir(dt))
print(dt.target)
print(dt.target_names)
x_train,x_test,y_train,y_test=train_test_split(dt.data,dt.target,test_size=0.2)
md.fit(x_train,y_train)
print(dt.data[:5])
print(md.predict(x_test))
print(md.score(x_test,y_test))

from sklearn.metrics import confusion_matrix
y_predicted=md.predict(x_test)
cm=confusion_matrix(y_test,y_predicted)
print(cm)
plt.figure(figsize=(10,8))
sns.heatmap(cm,annot=True)
plt.xlabel("predicted values")
plt.ylabel("actual values ")
plt.show()






