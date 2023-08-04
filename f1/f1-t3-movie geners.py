genres = {
    "Horror": 0,
    "Romance": 0,
    "Comedy": 0,
    "History": 0,
    "Adventure": 0,
    "Action": 0
}

count = int(input())
for i in range(0, count):
    entry = input().split()
    for j in entry[1:]:
        genres[j] += 1

genres = sorted(genres.items(), key=lambda t:t[0])
genres = sorted(genres, key=lambda t:t[1], reverse=True)
for i in genres:
    print("{} : {}".format(i[0], i[1]))