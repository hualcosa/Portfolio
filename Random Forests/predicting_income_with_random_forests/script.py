def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Loading the dataset
income_data = pd.read_csv("income.csv", header=0, delimiter= ", ")
# Take a glimpse at how the dataset is organized
#print(income_data.info())
#print(income_data.iloc[0])

# Separating the features and the labels
labels = income_data[["income"]]
'''
 the sex column is composed of strings("male and female) but the model only works
 with numbers. Then, we are going to create a column in which the  value 1
 represents a female and 0 a male.
'''
income_data["sex-int"] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)
'''
 There are a couple of other columns that use strings that might be useful to use.
 Let’s try transforming the values in the "native-country" column.
 ince the majority of the data comes from "United-States", it might make sense to
 make a column where every row that contains "United-States" becomes a 0 and any
 other country becomes a 1.
'''
income_data["native-country-int"] = income_data["native-country"].apply(lambda row: 0 if row == "United-States" else 1)

data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "native-country-int"]]

# Splitting the dataset
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1)

# Creating the model, fitting, getting the accuracy of the model with the test set
forest = RandomForestClassifier(random_state=1)
forest.fit(train_data, train_labels)
print(forest.score(test_data, test_labels))
# Checking the relevance of the different features of the model
print(forest.feature_importances_)