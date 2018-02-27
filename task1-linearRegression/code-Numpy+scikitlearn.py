#Tutorial: https://www.cnblogs.com/pinard/p/6016029.html

'''Data Preprocessing--Importing libraries'''
import numpy as np #for array manipulation'
import pandas as pd #for providing data structures--e.g. import dataset from online to be the input of the program'
import matplotlib.pyplot as plt #Python2D plotting library'
from sklearn import datasets, linear_model

'''Data Preprocessing--Importing dataset'''
dataset=pd.read_csv('/home/whh/Ubuntu/task1-linearRegression/CCPP/CCPP.csv') #file pathway. import csv file
#just for a preview: read first 5 lines of data. If read the last 5 lines, use data.tail()
dataset.head() 
#check dimension of dataset: result will be (#rows,#columns)
dataset.shape

'''Data Preprocessing--Define dependent variable--y and independent variables and put them into one vector--X''' 
X=dataset[['AT','V','AP','RH']]
X.head()
y=dataset[['PE']]
y.head()

'''Data Preprocessing--Taking care of missing data
#note: some data is missing and make the program invalid to run
from sklearn.preprocessing import Imputer #Imputer is a defined object in package. 
imputer=Imputer(missing_values =  'NaN',strategy = 'mean',axis=0) #assume in csv dataset, all missing data is represented by 'NaN'; strategy=mean, axis=0 --> use mean of the column(axis=0 for column) to replace the MISSED value.
imputer.fit(X[:,..:..]) #fit is only a function of object Imputer, and fit ONLY columns that contains missing data in the matrix X. (Please observe the missing data's col and put index above in ..:..
X[:,..:..]=imputer.transform(X[:,..:..]) #missed data is replaced in the corresponding columns in matrix.
'''

'''----------------DATA PREPROCESSING above, come from this tutorial-----------------https://www.udemy.com/deeplearning/learn/v4/t/lecture/6745258?start=0 This lecture section 29-- step 1-3
'''

'''Separate dataset to 'training set'--for generating model and 'test set'--for testing model '''
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

'''Linear regression on the data'''
from sklearn.linear_model import LinearRegression 
reg=LinearRegression()
reg.fit(X_train,y_train)
print (reg.coef_ )
print (reg.intercept_)

'''Evaluate model:''' 
y_pred=reg.predict(X_test)
#calculate MSE and RMSE -- the lower the better
from sklearn import metrics
print ("MSE:",metrics.mean_squared_error(y_test,y_pred))
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


'''Continuous Improving model:
Step 1. Maybe not all parameter in X is significant to output y-- to determine which parameters are important and need to stay, use Ridge Regression and LASSO-- http://statweb.stanford.edu/~tibs/sta305files/Rudyregularization.pdf -- code to be learned and added

Step 2. Maybe the choice of training set and test set has bias, to avoid this, use cross-validation-- e.g. k-fold cross validation(usually 10-fold--> cv=10)
NOTE: Results from cross-validation is MORE RELIABLE even if its MSE or RMSE may be larger than original results  
'''
X = dataset[['AT', 'V', 'AP', 'RH']]
y = dataset[['PE']]
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(reg, X, y, cv=10)
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y, predicted))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y, predicted)))



'''plot y_pred vs. y_measured'''
fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()


 















