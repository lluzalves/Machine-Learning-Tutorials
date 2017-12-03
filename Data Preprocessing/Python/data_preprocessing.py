# -*- coding: utf-8 -*-
# Importing the libaries 
import numpy as np
import matplotlib.pyplot as mathplot
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Data.csv')

# defining matrix of features include all lines and  all columns except the last
X = dataset.iloc[:, :-1].values

#defining the dependent variable vector
y = dataset.iloc[:, 3].values

#handling missing data  using Imputer class from sklearn to completing missing values
from sklearn.preprocessing import Imputer

# In this case the essential paramenters we need to achieve the imputatation transformation are the missing values 
# which is show as nan in our current dataset, we will make use of the mean strategy and to do that our axis will 
# be the columns of feature
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# now we need to fit  in our matrix more precisly in the columns were we have the missing values which is 1 and 2
imputer = imputer.fit(X[:,1:3])

# after fit we can replace the missing data by the mean of the columns using transform
X[:,1:3] = imputer.transform(X[:, 1:3])


