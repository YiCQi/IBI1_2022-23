# This code aims to use a formula to calculate the number of all elements in 5 cases.
# A loop was set to handle 5 cases, n is the sequence number and h is the result in every case.

# Set a loop from 1 to 5
for n in range(1,6):
    # Create formulas using known rules
    h = 2*n*(2*n-1)/2
    print(h)
  
# output:   1.0
#           6.0
#           15.0
#           28.0
#           45.0
