words_list = []

lines = input().split('. ')
words_count = 0

for i in range(0, len(lines)):
    words = lines[i].split()
    for j in range(1, len(words)):
        if words[j][0].isupper() and words[j][1].islower():
            words_list.append([
                words_count + 1 + j,
                words[j].strip(',').strip('.')
            ])
    words_count += len(words)

if len(words_list):
    for word in words_list:
        print("{}:{}".format(word[0], word[1]))
else:
    print("None")