'''
In this project, we will use perceptrons to model the fundamental
building blocks of computers — logic gates.
'''
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

'''
To begin, let’s think of an AND gate as a dataset of four points.
The four points should be the four possible inputs to the AND gate.
For example, the first point in the dataset should be [0, 0].

Create a variable named data that is a list that contains the four
possible inputs to an AND gate.
'''
data = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [0, 0, 0, 1]

'''
Let’s plot these four points on a graph.
'''
plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels)

'''
Now that we have our data, let’s build a perceptron to learn AND.
Create a Perceptron object named classifier. For now, set the
parameter max_iter to 40.

max_iter sets the number of times the perceptron loops through
the training data. The default is 1000, so we’re cutting the 
training pretty short! Let’s see if our algorithm learns AND even 
with very little training.
'''
classifier = Perceptron(max_iter = 40)

'''
We’ll now train the model.
'''
classifier.fit(data, labels)

'''
Let’s see if the algorithm learned AND.
'''
print(classifier.score(data, labels))

'''
Let's create a Heat Map that will allow us to see the decision Boundary!
Change the labels with you want to see how the decision boundary changes as you
train for another logical gate
'''
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)
abs_distances = [abs(d) for d in distances]
distances_matrix = np.reshape(abs_distances, (100,100))
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)

plt.show()

'''
Your perceptron should have 100% accuracy! You just taught it an AND gate!

Let’s change the labels so your data now represents an XOR gate. The label
should be a 1 only if one of the inputs is a 1. What is the accuracy of the
perceptron now? Is the data linearly separable?
'''
data = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [0, 1, 1, 0]

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels)
plt.show()

classifier = Perceptron(max_iter = 40)
classifier.fit(data, labels)
print(classifier.score(data, labels))