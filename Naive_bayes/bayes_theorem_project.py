import numpy as np
'''
Dr. Dirac's Statistics Midterm
Grading a multiple choice exam is easy. But how much do multiple choice exams tell us about what a student really knows? Dr. Dirac is administering a statistics midterm exam and wants to use Bayes’ Theorem to help him understand the following:

Given that a student answered a question correctly, what is the probability that she really knows the material?
Dr. Dirac knows the following probabilities based on many years of teaching:

There is a question on the exam that 60% of students know the correct answer to.
Given that a student knows the correct answer, there is still a 15% chance that the student picked the wrong answer.
Given that a student does not know the answer, there is still a 20% chance that the student picks the correct answer by guessing.
Using these probabilities, we can answer the question.
'''
# What is A and B in this case?
B = "student answered a question correctly"
A = "he really knows the material"

# What is the probability that the student knows the material?
p_a = 0.6

# Given that the student knows the material, what is the probability that she answers correctly?
p_b_given_a = 0.85

# What is the probability of any student answering correctly?
p_b = 0.6 * (1-0.15) + 0.4*0.2

# Using the three probabilities and Bayes’ Theorem, calculate P(knows material | answers correctly).
p_a_given_b = p_b_given_a * p_a / p_b
print(p_a_given_b)

