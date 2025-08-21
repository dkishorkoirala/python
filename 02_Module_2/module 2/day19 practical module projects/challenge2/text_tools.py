def count_words(text):
    words = text.split()
    return len(words)

def count_vowel(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def reverse_text(text):
    return text[::-1]
