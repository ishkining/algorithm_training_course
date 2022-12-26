number = int(input())
result_array = []
division = 2

while number != 1 or (division // 2) < number:
    if number % division == 0:
        number /= division
        result_array.append(division)
    else:
        division += 1

print(*result_array)