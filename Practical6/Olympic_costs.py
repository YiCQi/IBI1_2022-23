# This code uses pyplot to draw a bar chart.
# Olympic_Games is a list contains Olympic games recent years.
# costs is a list contains the cost of these Olympic games.
# sorted_costs is a list which is the sorted list of costs.
# The chart will show the sorted costs.

import matplotlib.pyplot as plt

# create a list which contains the cost of these Olympic games
costs=[1,8,15,7,5,14,43,40]
# make the list sorted
sorted_costs = sorted(costs)

# create a list which contains Olympic games recent years
Olympic_Games = ['Los Angeles 1984',
                      'Seoul 1988',
                      'Barcelona 1992',
                      'Atlanta 1996',
                      'Sydney 2000',
                      'Athens 2003',
                      'Beijing 2008',
                      'London 2012']

# show the sorted list
print(sorted_costs)

# create a bar chart and modify its style
plt.figure(figsize=(10,6))
plt.bar(Olympic_Games,sorted_costs,color = 'pink')
plt.xticks(fontsize = 8)

# Create x-axis and y-axis headings
plt.xlabel('Olympic Games', color = "green")
plt.ylabel('costs', color = "green")

# make grid
plt.grid(True)

plt.show()
