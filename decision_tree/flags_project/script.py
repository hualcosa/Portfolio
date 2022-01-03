import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

'''
Find the Flag
Can you guess which continent this flag comes from?
What are some of the features that would clue you in? Maybe some of the colors are good indicators. The presence or absence of certain shapes could give you a hint. In this project, we’ll use decision trees to try to predict the continent of flags based on several of these features.

We’ll explore which features are the best to use and the best way to create your decision tree.
'''

flags = pd.read_csv("flags.csv", header=0)
# Take a look that the informations about the dataset if you will
#flags.info()
#print(flags.head())

'''
Many columns contain numbers that don’t make a lot of sense. For example, the third row, which represents Algeria, has a Language of 8. What exactly does that mean?

Take a look at the Attribute Information for this dataset from UCI’s Machine Learning Repository: http://archive.ics.uci.edu/ml/datasets/Flags
'''

# separating the labels and the data features
labels =flags['Landmass']
data = flags[["Red", "Green", "Blue", "Gold","White", "Black", "Orange","Circles","Crosses","Saltires","Quarters","Sunstars",
              "Crescent","Triangle"]]

# Splitting the data
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)

# Investigating corralation between the tree's depth and accuracy of the model
scores = []
for i in range(1, 21):
  tree = DecisionTreeClassifier(random_state=1, max_depth=i)
  tree.fit(train_data, train_labels)
  scores.append(tree.score(test_data, test_labels))
# Ploting the results
plt.plot(range(1, 21), scores)
plt.xlabel("Tree's depth")
plt.ylabel("Accuracy")
plt.show()

  
