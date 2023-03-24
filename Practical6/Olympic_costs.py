# This code uses pyplot to draw a pie chart.
# movie_genres is a dictionary whose key shows the genres
# and value shows the number of students who like the genre most.
# movie_genres is printed.
# You can modify the chosen genre which will also be printed.
# The pie chart will be shown in a new window.

import matplotlib.pyplot as plt

# create a dictionary contains movie genres and numbers of students who like the genre most.
movie_genres = {'Comedy':73,
                'Action':42,
                'Romance':38,
                'Fantasy':28,
                'Science-fiction':22,
                'Horror':19,
                'Crime':18,
                'Documentary':12,
                'History':8,
                'War':7}

# print movie genres
print(movie_genres)

# choose a genre and print the number of students who like this genre most
chosen_genre = 'Comedy' # The variable I choose is Comedy. It can be modified.
print(movie_genres[chosen_genre])

# draw the pie chart
plt.pie(movie_genres.values(), labels=movie_genres.keys(), autopct='%1.1f%%')
plt.title('Movie Genres')
plt.show()
