'''Data Preprocessing--Importing libraries'''
import numpy as np #for array manipulation'
import pandas as pd #for providing data structures--e.g. import dataset from online to be the input of the program'
import matplotlib.pyplot as plt #Python2D plotting library'

'''Data Preprocessing--Importing dataset'''
dataset=pd.read_csv('/home/whh/Ubuntu/task1-linearRegression/kc_house_data.csv') #file pathway. import csv file
#dataset.columns = ['col1','col2'] #give them col(variable) names
#dateset.head() #just for a preview:this can display data into a table with column name created above using .columns

#assume in csv file provided, the last column is Dependent Variable--y, the rest columns are indep variables--X. 
X=dataset.iloc[:,3].values #X is a multi-col array; Note:iloc is a PANDA function, for selection by position/index
X=X.reshape(-1,1)
y=dataset.iloc[:,2].values
print (X,y)

'''Data Preprocessing--Taking care of missing data
#note: some data is missing and make the program invalid to run
from sklearn.preprocessing import Imputer #Imputer is a defined object in package. 
imputer=Imputer(missing_values =  'NaN',strategy = 'mean',axis=0) #assume in csv dataset, all missing data is represented by 'NaN'; strategy=mean, axis=0 --> use mean of the column(axis=0 for column) to replace the MISSED value.
imputer.fit(X[:,..:..]) #fit is only a function of object Imputer, and fit ONLY columns that contains missing data in the matrix X. (Please observe the missing data's col and put index above in ..:..
X[:,..:..]=imputer.transform(X[:,..:..]) #missed data is replaced in the corresponding columns in matrix.
'''

'''----------------DATA PREPROCESSING above, come from this tutorial-----------------https://www.udemy.com/deeplearning/learn/v4/t/lecture/6745258?start=0 This lecture section 29-- step 1-3
'''




'''Linear regression on the data'''
from sklearn.linear_model import LinearRegression 

from sklearn.preprocessing import scale

reg=LinearRegression()
reg.fit(X,y)
slope=reg.coef_(0)
intercept=reg.intercept_

#plot-- For one indep vari X only. (NO x1,x2... in X matrix)
plt.scatter(X,y,color='black')
predicted_values=[slope * i + intercept for i in X]
plt.plot(X,predicted_values,'b')
plt.xlabel("name of x")
plt.ylabel("name of y")

#IF want to predict y given x,e.g.: 
reg.predict(X=6.2)
















