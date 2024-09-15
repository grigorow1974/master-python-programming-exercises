# Your code here
def letters_and_digits(text):
    letters = 0
    digits = 0
    for x in text:
        if x.isdigit():
            digits +=1
        elif x.isalpha():
            letters += 1
    print (f'LETTERS: {letters}')
    print (f'DIGITS: {digits}')


letters_and_digits("hello world! 123")