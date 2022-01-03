import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()


'''
If you will, uncomment this box to discover informations
about the dataset
'''
#print(digits)
#print(digits.DESCR)
#print(digits.data)
#print(digits.target)

'''
To visualize the data images, we need to use Matplotlib.
Let’s visualize the image at index 100
'''
plt.gray() 

plt.matshow(digits.images[100])

plt.show()
print(digits.target[100])

# Take a look at 64 sample images

# Figure size (width, height)

fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images

for i in range(64):

    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position

    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value

    ax.text(0, 7, str(digits.target[i]))

plt.show()

# Import KMeans from sklearn.cluster.
from sklearn.cluster import KMeans

# Create the model
model = KMeans(n_clusters = 10, random_state = 42)

# Fit the model
model.fit(digits.data)


'''
Let’s visualize all the centroids! Because data samples live in
a 64-dimensional space, the centroids have values so they can be
images!
'''
fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()