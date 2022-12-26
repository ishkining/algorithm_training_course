(a, b, c) = (int(number) % 2 for number in input().split(' '))
result = 'WIN' if a == b == c else 'FAIL'
print(result)