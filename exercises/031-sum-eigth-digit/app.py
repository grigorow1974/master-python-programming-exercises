# Your code here
def all_digits_even():
    for x in range (1000,3001):
        if x % 2 == 0:
            print(f'{x}', end = ',')

all_digits_even()