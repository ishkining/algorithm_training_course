import math

number = int(input())
degree = None
result = ['0'] * (math.floor(math.log2(number)) + 1)

while True:
    print(number, ' ', degree)
    if degree is not None:
        result[degree] = '1'
        number -= 2 ** degree
        if number <= 0:
            break

    degree = math.floor(math.log2(number))

print(''.join(result[::-1]))
