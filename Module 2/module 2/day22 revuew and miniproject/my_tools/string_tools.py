def word_count(word):
    return len(word.replace(" ", ""))

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else :
        return False

def word_rev(word):
    return word[::-1]