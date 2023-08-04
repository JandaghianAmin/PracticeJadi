def isPrime(num):
    if num > 1:
        x = True
        for i in range(2, num-1):
            if (num % i) == 0:
                x = False
                break
        return x
    return False

def divcount(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0 and isPrime(i):
            count += 1
    return count
max = 0
max_div_count = 0
for i in range(0, 10):
    num = int(input())
    div_count = divcount(num)
    if max_div_count < div_count:
        max = num
        max_div_count = div_count
    elif max_div_count == div_count and max < num:
        max = num
print(max, max_div_count)