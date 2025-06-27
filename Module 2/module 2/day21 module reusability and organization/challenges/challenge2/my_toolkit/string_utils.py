def count_words(word):
    return len("".join(word.split()))

def is_palindrom(word):
    if word == word[::-1]:
        return f"YES the word is palindrome"
    else:
        return f"NOT a palindrome"
    