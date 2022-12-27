import sys


def main():
    n = int(input())
    m = int(input())
    matrix = []
    result = [[] for _ in range(m)]
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        matrix.append(line.split())
    for column_index in range(m):
        for row_index in range(n):
            result[column_index].append(matrix[row_index][column_index])

    print(result)


if __name__ == '__main__':
    main()

