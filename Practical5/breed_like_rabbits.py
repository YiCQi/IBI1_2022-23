# This code aims to calculate the generations taken to multiply the rabbits to the number of 100.
# The original number of rabbits( n ) is 2 and the original generation( g ) is 1.
# Every new generation( g += 1 ) the number of rabbits doubles( n *= 2 ).
# generation( g ) will be printed as the result.

n = 2 # The original number of rabbits 
g = 1 # Generation of rabbits
# when rabbits number is larger than 100, end loop
while n <= 100:
    # every new generation the number of rabbits doubles
    g += 1
    n *= 2
print(g)

# answer: it takes 7 generations
