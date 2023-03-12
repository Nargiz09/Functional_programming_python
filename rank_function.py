def number_of_ranks(value):
    number = 0
    while value > 0:
        value //= 10
        number += 1
    return number
value = int(input('Enter the number: '))
print('Number of ranks:', number_of_ranks(value))