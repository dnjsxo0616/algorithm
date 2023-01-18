word = input()
# lit = ['C','A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
words = 'CAMBRIDGE'
for i in range(len(words)):
    word = word.replace(words[i],'')
print(word)