#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

ax = plt.subplot()
plt.bar(range(len(games)), viewers, color='purple')
plt.title('Top 10 popular games in Twitch')
plt.xlabel('game')
plt.ylabel('Viewers on January')
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=60)
plt.show()
plt.clf()


# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
plt.pie(countries, colors=colors, explode=explode, autopct='%1.0d%%', pctdistance=1.15 ,shadow=True, startangle=345)
plt.axis('equal')
plt.title("League of Legends Viewers's Whereabouts")
plt.legend(labels, loc='right')
plt.show()
plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
y_upper = [h * (1 + 0.15) for h in viewers_hour]
y_lower = [h *(1 - 0.15) for h in viewers_hour]

ax = plt.subplot()
plt.fill_between(hour, y_upper, y_lower, alpha=0.2, color='pink')
plt.plot(hour, viewers_hour, color='white')
plt.title('Number of Viewers per Hour')
plt.xlabel('hour')
plt.ylabel('Viewers')
ax.set_xticks(hour)
ax.set_facecolor('slateblue')
plt.legend(['January 1st, 2015'])
plt.show()
plt.clf()