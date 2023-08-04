names = []

count = int(input())
for i in range(0, count):
    entry = input().split('.')
    names.append([
        entry[0],
        str(entry[1]).capitalize(),
        entry[2]
    ])

names = sorted(names, key=lambda t:t[1])
names = sorted(names, key=lambda t:t[0])
for i in names:
    print(i[0], i[1], i[2])