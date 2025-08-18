def word_count(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else: 
            freq[word] = 1
    return freq