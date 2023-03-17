n = 2 # The original number of rabbits 
g = 1 # Generation of rabbits
# when rabbits number is larger than 100, end loop
while n <= 100:
    # every new generation the number of rabbits doubles
    g += 1
    n = 2 ** g
print(g)

# answer: it takes 7 generations
