def count_words(word):
    return len(word)

def is_palindrom(word):
    if word == word[::-1]:
        return f"YES the word is palindrome"
    else:
        return f"NOT a palindrome"
    