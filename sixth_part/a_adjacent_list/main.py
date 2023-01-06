import sys


def main():
    line = sys.stdin.readline().rstrip().split(' ')
    n = int(line[0])
    m = int(line[1])
    adj_list = [[0, []] for _ in range(n)]
    for _ in range(m):
        line = sys.stdin.readline().rstrip().split(' ')
        adj_list[int(line[0]) - 1][0] += 1
        (adj_list[int(line[0]) - 1][1]).append(int(line[1]))

    for index in range(len(adj_list)):
        if len(adj_list[index][1]) > 0:
            adj_list[index][1].sort()
        print(adj_list[index][0], ' ', *adj_list[index][1])


if __name__ == '__main__':
    main()