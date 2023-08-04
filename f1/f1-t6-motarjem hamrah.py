translate_words = []

count = int(input())
for i in range(0, count):
    translate_words.append(input().split())

entry_line = input()
translated_line = ""

for word in entry_line.split():
    word_found = word
    for translate_word in translate_words:
        if word in translate_word[1:]:
            word_found = translate_word[0]
            break
    translated_line = translated_line + word_found + " " 

print(translated_line.strip())