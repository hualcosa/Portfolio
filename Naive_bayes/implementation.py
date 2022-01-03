'''
I couldn't download the dataset. But at least you can take a look on how i 
implemmented the classifier. 'pos_counter' and 'neg_counter' were dictionaires with
the frequencies for each word present in the positive reviews
subset and negative reviews reviews subset
'''
#from reviews import neg_counter, pos_counter

review = "This product sucks!"

percent_pos = 0.5
percent_neg = 0.5

total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

pos_probability = 1
neg_probability = 1

review_words = review.split()

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))

final_pos = pos_probability * percent_pos
final_neg = neg_probability * percent_neg
print(final_pos)
print(final_neg)

if final_pos > final_neg:
  print("The review is positive")
else:
  print("The review is negative")
