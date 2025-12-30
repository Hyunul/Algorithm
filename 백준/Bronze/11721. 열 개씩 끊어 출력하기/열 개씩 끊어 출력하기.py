import sys
input = sys.stdin.readlines

word = input()[0]
word_list = []

i = 0
j = 10
for _ in range(len(word) // 10 + 1):
    print(word[i:j])
    i += 10
    j += 10