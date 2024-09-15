# Your code here
def remove_duplicate_words(text):
    text = text.split(' ')
    print (" ".join(sorted(set(text))))


remove_duplicate_words ("hello world and practice makes perfect and hello world again")