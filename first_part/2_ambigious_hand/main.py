k = int(input())
result = []
number_line = ''
for _ in range(4):
    number_line += input()

while len(number_line) > 0:
    if number_line.count(number_line[0]) <= 2 * k and number_line[0] != '.':
        result.append(number_line[0])
    number_line = number_line.replace(number_line[0], '')
print(len(result))