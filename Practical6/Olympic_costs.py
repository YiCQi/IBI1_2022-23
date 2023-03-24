# This code uses pyplot to draw a bar chart.
# Olympic_Games_costs is a dictionary contains Olympic games and their costs recent years.
# costs is a list contains the cost of these Olympic games.
# sorted_costs is a list which is the sorted list of costs.
# sorted_Games will be added in sorted Olympic Games.
# The chart will show the sorted costs and matched Olympic Games.

import matplotlib.pyplot as plt

# create a list which contains the cost of these Olympic games
costs=[1,8,15,7,5,14,43,40]
# make the list sorted
sorted_costs = sorted(costs)

# create a list which contains Olympic games and their costs recent years
Olympic_Games_costs = {1:'Los Angeles 1984',
                 8:'Seoul 1988',
                 15:'Barcelona 1992',
                 7:'Atlanta 1996',
                 5:'Sydney 2000',
                 14:'Athens 2003',
                 43:'Beijing 2008',
                 40:'London 2012'}

# create sorted_Games
sorted_Games = []
for cost in sorted_costs:
    sorted_Games.append(Olympic_Games_costs[cost])

# show the sorted list
print(sorted_costs)


# create a bar chart and modify its style
plt.figure(figsize=(10,6))
colors = ['pink','blue','brown','green']
plt.bar(sorted_Games,sorted_costs,color = colors)
plt.xticks(fontsize = 8)

# Create x-axis and y-axis headings
plt.xlabel('Olympic Games', color = "green")
plt.ylabel('costs', color = "green")

# make grid
plt.grid(True)

plt.show()
