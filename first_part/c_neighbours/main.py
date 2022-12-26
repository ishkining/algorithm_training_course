n = int(input())
m = int(input())
matrix = []
for index_row in range(n):
    matrix.append([int(number) for number in input().split(' ')])
a = int(input())
b = int(input())

result = []
if a != 0:
    result.append(matrix[a - 1][b])
if a != n - 1:
    result.append(matrix[a + 1][b])

if b != 0:
    result.append(matrix[a][b - 1])
if b != n - 1:
    result.append(matrix[a][b + 1])

print(result)