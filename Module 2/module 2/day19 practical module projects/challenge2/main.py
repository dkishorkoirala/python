from text_tools import count_words, count_vowel, reverse_text

text = input("Enter the sentence: ")

print(f"\nWord Count: {count_words(text)}")
print(f"\nVowel count: {count_vowel(text)}")
print(f"\nReverse of sentence: {reverse_text(text)}")
