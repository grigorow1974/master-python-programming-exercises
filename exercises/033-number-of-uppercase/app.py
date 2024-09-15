# Your code here
# Your code here
def number_of_uppercase(text):
    UPPER = 0
    LOWER = 0
    for x in text:
        if x.isupper():
            UPPER +=1
        elif x.islower():
            LOWER += 1
    print (f'UPPER: {UPPER}')
    print (f'LOWER: {LOWER}')


number_of_uppercase("HeLlo WorlD")