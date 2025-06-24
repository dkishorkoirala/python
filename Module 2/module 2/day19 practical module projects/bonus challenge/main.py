from word_status import word_count

sentence = input("Enter a sentence: ")

print("\nWord Frequency:")
result = word_count(sentence)
for word, count in result.items():
    print(f"{word} - {count}")