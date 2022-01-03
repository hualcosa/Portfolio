import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())
print(df.columns)
print(df.describe())

'''
Player: name of the tennis player
Year: year data was recorded

Service Game Columns (Offensive)

Aces: number of serves by the player where the receiver does not touch the ball
DoubleFaults: number of times player missed both first and second serve attempts
FirstServe: % of first-serve attempts made
FirstServePointsWon: % of first-serve attempt points won by the player
SecondServePointsWon: % of second-serve attempt points won by the player
BreakPointsFaced: number of times where the receiver could have won service game of the player
BreakPointsSaved: % of the time the player was able to stop the receiver from winning service game when they had the chance
ServiceGamesPlayed: total number of games where the player served
ServiceGamesWon: total number of games where the player served and won
TotalServicePointsWon: % of points in games where the player served that they won

Return Game Columns (Defensive)

FirstServeReturnPointsWon: % of opponents first-serve points the player was able to win
SecondServeReturnPointsWon: % of opponents second-serve points the player was able to win
BreakPointsOpportunities: number of times where the player could have won the service game of the opponent
BreakPointsConverted: % of the time the player was able to win their opponent’s service game when they had the chance
ReturnGamesPlayed: total number of games where the player’s opponent served
ReturnGamesWon: total number of games where the player’s opponent served and the player won
ReturnPointsWon: total number of points where the player’s opponent served and the player won
TotalPointsWon: % of points won by the player

Outcomes

Wins: number of matches won in a year
Losses: number of matches lost in a year
Winnings: total winnings in USD($) in a year
Ranking: ranking at the end of year
'''
# perform exploratory analysis here:
print(df.corr())

plt.scatter(df['FirstServeReturnPointsWon'],df['Winnings'])
plt.title('FirstServeReturnPointsWon vs Winnings')
plt.xlabel('FirstServeReturnPointsWon')
plt.ylabel('Winnings')
plt.show()
plt.clf()

plt.scatter(df['BreakPointsOpportunities'], df['Winnings'])
plt.title('BreakPointsOpportunities vs Winnings')
plt.xlabel('BreakPointsOpportunities')
plt.ylabel('Winnings')
plt.show()
plt.clf()

plt.scatter(df['BreakPointsSaved'], df['Winnings'])
plt.title('BreakPointsSaved vs Winnings')
plt.xlabel('BreakPointsSaved')
plt.ylabel('Winnings')
plt.show()
plt.clf()

plt.scatter(df['TotalPointsWon'],df['Ranking'])
plt.title('TotalPointsWon vs Ranking')
plt.xlabel('TotalPointsWon')
plt.ylabel('Ranking')
plt.show()
plt.clf()

plt.scatter(df['TotalServicePointsWon'], df['Wins'])
plt.title('TotalServicePointsWon vs Wins')
plt.xlabel('TotalServicePointsWon')
plt.ylabel('Wins')
plt.show()
plt.clf()





## perform single feature linear regressions here:
# Let's investigate the correlation between FirstServeReturnPointsWon and Wins
features = df[['FirstServeReturnPointsWon']]
winnings = df[['Wins']]

# Train, test, split the data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size=0.8)

# Create and train the model on train data
regressor = LinearRegression()
regressor.fit(features_train, winnings_train)

# Assesing the model score with test data
print('Predicting Winnings with FirstServeReturnPointsWon Test Score:', regressor.score(features_test,winnings_test))

# Making predictions with the model
winnings_prediction = regressor.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - 1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## single feature linear regression (BreakPointsOpportunities)

# select features and value to predict
features = df[['BreakPointsOpportunities']]
winnings = df[['Winnings']]

# train, test, split the data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size = 0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train,winnings_train)

# score model on test data
print('Predicting Winnings with BreakPointsOpportunities Test Score:', model.score(features_test,winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - 1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## single feature linear regression (BreakPointsOpportunities)

# select features and value to predict
features = df[['BreakPointsOpportunities']]
winnings = df[['Winnings']]

# train, test, split the data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size = 0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train,winnings_train)

# score model on test data
print('Predicting Winnings with BreakPointsOpportunities Test Score:', model.score(features_test,winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - 1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## two feature linear regression

# select features and value to predict
features = df[['BreakPointsOpportunities','FirstServeReturnPointsWon']]
winnings = df[['Winnings']]

# train, test, split the data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size = 0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train,winnings_train)

# score model on test data
print('Predicting Winnings with 2 Features Test Score:', model.score(features_test,winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - 2 Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## multiple features linear regression

# select features and value to predict
features = df[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon','SecondServePointsWon','SecondServeReturnPointsWon','Aces','BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities','BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon','ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon','TotalServicePointsWon']]
winnings = df[['Winnings']]

# train, test, split the data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size = 0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train,winnings_train)

# score model on test data
print('Predicting Winnings with Multiple Features Test Score:', model.score(features_test,winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - Multiple Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()



