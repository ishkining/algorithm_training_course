first_binary_number = [int(number) for number in input()]
second_binary_number = [int(number) for number in input()]
memory = 0
result = ''

while len(first_binary_number) > 0 or len(second_binary_number) > 0 or memory == 1:
    first_contestant = 0
    second_contestant = 0
    if len(first_binary_number) > 0:
        first_contestant = first_binary_number.pop()
    if len(second_binary_number) > 0:
        second_contestant = second_binary_number.pop()
    sum_of_two = first_contestant + second_contestant + memory
    result += str(sum_of_two % 2)
    if sum_of_two >= 2:
        memory = 1
    else:
        memory = 0

print(result[::-1])