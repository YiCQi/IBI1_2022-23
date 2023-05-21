# What does this piece of code do?
# Answer: Choose 10 numbers randomly from 1 to 100, select the max number in these 10 numbers and print it.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# Set initial progress
progress=0
# Processed variable
stored_random_number=0
# Set a loop, choose 1 max number from 10 numbers
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
