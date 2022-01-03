#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Importing the dataset
breast_cancer_data = load_breast_cancer()
# Investigating the characteristics of the data
# print(breast_cancer_data.data[0])
# print(breast_cancer_data.feature_names)
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

# Splitting the dataset
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)
# If the data was splitted correctly the two following parts should have the same length
#print(len(training_data))
#print(len(training_labels))

# Cheking the model accuracy
k_list = range(1, 101)
accuracies = []
for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(training_data, training_labels)
    accuracies.append(classifier.score(validation_data, validation_labels))

plt.plot(k_list, accuracies)
plt.title("Breast Cancer Classifier Accuracy")
plt.xlabel('K value')
plt.ylabel('Validation Accuracy')
plt.show()
plt.clf()