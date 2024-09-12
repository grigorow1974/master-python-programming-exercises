# Your code here
def sequence_of_words(words):
    words =words.split(",")
    words.sort()
    result = ', '.join(words)
    print(result)

sequence_of_words("without,hello,bag,world")