import sys


def main():
    line = sys.stdin.readline().rstrip().split(' ')
    n = int(line[0])
    m = int(line[1])
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        adj_matrix[int(line[0]) - 1][int(line[1]) - 1] = 1

    for row in adj_matrix:
        print(*row)


if __name__ == '__main__':
    main()
