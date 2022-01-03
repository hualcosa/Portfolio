'''
As you may have already heard, the honeybees are in a precarious state right
now. You may have seen articles about the decline of the honeybee population
for various reasons. You want to investigate this decline and how the trends
of the past predict the future for the honeybees.
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# importing the dataset
df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df.head())
print(df.columns)

# get the mean of totalprod per year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
print(prod_per_year)

'''
Create a variable called X that is the column of years in this prod_per_year
DataFrame.
After creating X, we will need to reshape it to get it into the right format.
'''
X = prod_per_year['year']
X = X.values.reshape(-1, 1)

'''
Create a variable called y that is the totalprod column in the prod_per_year
dataset.
'''
y = prod_per_year['totalprod']

# Create a linear regression model from scikit-learn and call it regr.
regr = linear_model.LinearRegression()

# fit the model to the data
regr.fit(X, y)

'''
After you have fit the model, print out the slope of the line and the
intercept of the line.
'''
print(regr.coef_)
print(regr.intercept_)

'''
Create a list called y_predict that is the predictions your regr model
would make on the X data.
'''
m = regr.coef_
b = regr.intercept_
y_predict = [m*el + b for el in X]

'''
Our known dataset stops at the year 2012, so let’s create a NumPy array called
X_future that is the range from 2013 to 2050
'''
X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)

'''
Create a list called future_predict that is the y-values that your regr model
would predict for the values of X_future.
'''
future_predict = regr.predict(X_future)


'''
Using plt.scatter(), plot y vs X as a scatterplot. 
Plot y_predict vs X as a line, on top of your scatterplot
'''
plt.scatter(X, y)
plt.title('Total production of Honey per year')
plt.xlabel('year')
plt.ylabel('Production of honey')
plt.plot(X, y_predict)
plt.show()

# Plot future_predict vs X_future on a different plot.
plt.plot(X_future, future_predict)
plt.title('Total production of Honey per year')
plt.xlabel('year')
plt.ylabel('Production of honey')
plt.show()
