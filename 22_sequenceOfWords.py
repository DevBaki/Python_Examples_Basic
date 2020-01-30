stringInput = input()
wordsDic = {}

for word in stringInput.split():
    wordsDic[word] = wordsDic.get(word, 0) + 1

print(wordsDic)
