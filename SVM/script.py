import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

'''
I was not able to get the dataset for these three players at line 6 with codecamy
but in this folder there is a image that ilustres the result of executing the program
with the dataset. Sorry :(
'''

def show_results(athlete):
  fig, ax = plt.subplots()
  athlete['type'] = athlete['type'].map({'S':1,'B':0 })
  athlete = athlete.dropna(subset = ['plate_x', 'plate_z', 'type'])

  plt.scatter(athlete['plate_x'], athlete['plate_z'], c=athlete['type'], cmap=plt.cm.coolwarm, alpha=0.25)
  plt.xlabel('X coordinate')
  plt.ylabel('Z coordiante')
  plt.title('Red: Strike   Blue: Ball')
  training_set, validation_set = train_test_split(athlete, random_state=1)

# Tunning the model to find the best C and gamma parameters
  scores = [0]
  max_parameters = []
  for i in range(1, 10):
    for j in range(1, 10):
      classifier = SVC(kernel='rbf', gamma=i, C=j)
      classifier.fit(training_set[['plate_x', 'plate_z']],       training_set['type'])
      score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])
      if score > np.max(scores):
        max_parameters = [i, j]
      scores.append(score)
    
  classifier = SVC(kernel='rbf', gamma=max_parameters[0], C=max_parameters[1])
  classifier.fit(training_set[['plate_x', 'plate_z']],       training_set['type'])
  draw_boundary(ax, classifier)
  plt.show()
  plt.clf()
  # removing the 0 at the beginning of the vector
  scores = scores[1:]
  plt.scatter(range(1, len(scores) + 1), scores)
  # fixing the scale so that the difference between different players become more noticeable
  ax.set_ylim(-2, 6)
  ax.set_xlim(-3, 3)
  plt.show()

  print("The maximum accuracy achieved was {}".format(np.max(scores)))
  print("The C and alpha parameters that maximazes accuracy are: {}  {}".format(max_parameters[0], max_parameters[1]))

# call the function with different player names to compare the results
show_results(jose_altuve)