import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:

wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood_rankings.head())
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(steel_rankings.head())

# write function to plot rankings over time for 1 roller coaster here:
def roller_over_time(coaster, park, ranking):
    coaster_ranking = ranking[(ranking['Name'] == coaster) & (ranking['Park'] == park)]
    fig, ax = plt.subplots()
    ax.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'])
    ax.set_yticks(coaster_ranking['Rank'].values)
    ax.set_xticks(coaster_ranking['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title('{} rankings'.format(coaster))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()

roller_over_time('El Toro', 'Six Flags Great Adventure', wood_rankings)
plt.clf()



# write function to plot rankings over time for 2 roller coasters here:
def two_rankings_same_time(coaster1_name, park1_name, coaster2_name, park2_name, ranking):
    coaster1_ranking = ranking[(ranking['Name'] == coaster1_name) & (ranking['Park'] == park1_name)]
    coaster2_ranking = ranking[(ranking['Name'] == coaster2_name) & (ranking['Park'] == park2_name)]
    fig, ax =plt.subplots()
    ax.plot(coaster1_ranking['Year of Rank'], coaster1_ranking['Rank'], label=coaster1_name, color='Blue')
    ax.plot(coaster2_ranking['Year of Rank'], coaster2_ranking['Rank'], label=coaster2_name, color='Yellow')
    ax.invert_yaxis()
    ax.set_xticks(ranking['Year of Rank'].values)
    plt.title('{} vs {} rankings'.format(coaster1_name, coaster2_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking position')
    plt.legend()
    plt.show()

two_rankings_same_time('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood_rankings)
plt.clf()

# write function to plot top n rankings over time here:
def top_n_coasters(ranking_df, n):
    top_rankings = ranking_df[ranking_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(10,10))
    for coaster in set(top_rankings['Name']):
        coaster_rankings = top_rankings[top_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    ax.invert_yaxis()
    ax.set_yticks([i for i in range(1, n+1)])
    plt.title('Top {} coaster rankings'.format(n))
    plt.xlabel('Year')
    plt.ylabel('Ranking position')
    plt.legend(loc=4)
    plt.show()
    
top_n_coasters(wood_rankings,10)
plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv('roller_coasters.csv')
#print(roller_coasters.head())

# write function to plot histogram of column values here:
def plot_hist(coaster_df, column_name):
    plt.hist(coaster_df[column_name].dropna(), histtype='step', normed=True)
    plt.title('distribution of data from column {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

plot_hist(roller_coasters, 'speed')
plt.clf()
plot_hist(roller_coasters, 'length')
plt.clf()
plot_hist(roller_coasters, 'num_inversions')
plt.clf()

# function to plot histogram of height values
def plot_height_histogram(coaster_df):
    heights = coaster_df[coaster_df['height'] <= 140]['height'].dropna()
    plt.hist(heights)
    plt.title('Histogram of Roller Coaster Height')
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.show()

plot_height_histogram(roller_coasters)
plt.clf()

# write function to plot inversions by coaster at a park here:
def plot_inversions_per_coaster(coaster_df, park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(range(len(number_inversions)), number_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=90)
    plt.title('Number of inversions per coaster at {} park'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('# of Inversions')
    plt.show()

plot_inversions_per_coaster(roller_coasters, 'Six Flags Great Adventure')
plt.clf()

# write function to plot pie chart of operating status here:
def pie_chart_status(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)
    status_counts = [num_operating_coasters, num_closed_coasters]
    plt.pie(status_counts,autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.show()


pie_chart_status(roller_coasters)
plt.clf()


# write function to create scatter plot of any two numeric columns here:
def plot_scatter(coaster_df, column_x, column_y):
    plt.scatter(coaster_df[column_x], coaster_df[column_y])
    plt.title('Scatter plot of {} vs. {}'.format(column_y, column_x))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()

coaster_df = roller_coasters[roller_coasters['height'] < 140]
plot_scatter(coaster_df, 'height', 'speed')
plt.clf()
