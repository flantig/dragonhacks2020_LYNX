from collections import Counter

f = 'This is a test to see if I can make a count dictionary. This is this because this is this.'

def word_list(y):
    l = list(map(lambda  x: x, y.split()))
    return l

def word_counter(list):
    cntin = Counter()
    for word in list:
        cntin[word] += 1
    return cntin

banned_words = []

list_of_word = word_list(f)
most_common_words = Counter(word_list(f)).most_common(10)
print(most_common_words)


