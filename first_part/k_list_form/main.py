n_x = int(input())
x_array = [int(number) for number in input().split(' ')]
k_array = [int(number) for number in input()]
result = []

pivot = len(x_array) - 1
memory = 0

while memory == 1 or len(x_array) > 0 or len(k_array) > 0:
    first_number = 0
    second_number = 0
    if len(x_array) > 0:
        first_number = x_array.pop()
    if len(k_array) > 0:
        second_number = k_array.pop()

    result_sum = first_number + second_number + memory
    result.insert(0, result_sum % 10)
    memory = 1 if result_sum >= 10 else 0

print(*result)
