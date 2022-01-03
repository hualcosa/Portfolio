from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# If necessary, change the working directory
# path = os.getcwd()
# path = os.chdir(path)


# Load the dataframes
df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

# Create a new column in df named Total Goals, 
# and set it equal to the sum of the columns Home Team Goals and Away Team Goals.
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

# Set the style of your plot to be whitegrid . This will add gridlines to the plot
#  which will make it easier to read the visualization.
sns.set_style('whitegrid')

# Set the context to poster to make the visualisation bigger and easier to read.
sns.set_context('poster', font_scale=0.7)

# Create a figure and axes for your plot.
f, ax = plt.subplots(figsize=(12,7))

# visualize the columns Year and Total Goals as a bar chart.
year = df['Year']
total_goals = df['Total Goals']
ax = sns.barplot(data=df, x=year, y=total_goals)
ax.set_title('Total goals scored vs World Cup year')
plt.show()

# Create a box plot so you can visualize the distribution 
# of the goals data instead of just the average with a bar chart.
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
goals = df_goals['goals']
year = df_goals['year']
ax2 = sns.boxplot(data=df_goals, x=year, y=goals, palette='Spectral')
ax2.set_title('distribution of goals scored per match per World Cup')
plt.show()