# This is a project i have develloped during my data science path in Codecademy

'''
In this project, you will use scikit-learn’s Naive Bayes implementation on 
several different datasets. By reporting the accuracy of the classifier, 
we can find which datasets are harder to distinguish. For example, how 
difficult do you think it is to distinguish the difference between emails 
about hockey and emails about soccer? How hard is it to tell the difference
between emails about hockey and emails about tech? In this project, we’ll 
find out exactly how difficult those two tasks are.
'''

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

'''
We’re interested in seeing how effective our Naive Bayes classifier is at 
telling the difference between a baseball email and a hockey email. We can
select the categories of articles we want from fetch_20newsgroups by adding
the parameter categories.
'''
emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])

'''
Print emails.target_names to see the different categories.
'''
#print(emails.data[5])

'''
All of the emails are stored in a list called emails.data. Print the email at 
index 5 in the list.
'''
#print(emails.target[5])

'''
All of the labels can be found in the list emails.target. Print the label of
the email at index 5.
'''
#print(emails.target_names)

# Splitting the dataset
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='train', shuffle=True, random_state=108)
test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

# Creating counter, fitting and transforming the data
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# Creating the classifier, fitting the data and assessing the score of the model
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)
print(classifier.score(test_counts, test_emails.target)
)
