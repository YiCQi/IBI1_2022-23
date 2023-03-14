n = 2 # the original number of rabbits 
g = 1 # generation of rabbits
while n <= 100: # when number is larger than 100, end loop
    g += 1
    n = 2 ** g
print(g)

# answer: it takes 7 generations
