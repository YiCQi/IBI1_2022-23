# write a function which determines whether an individual can buy a specific house
def calculator(house_price,annual_salary):
    # buy a house worth no more than five times	your annual	salary
    if house_price <= annual_salary * 5:
        return 'Yes'
    else:
        return 'No'
# call
print(calculator(180000,35000))