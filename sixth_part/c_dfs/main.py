import sys


def dfs(start_index, length_dots, vertex):
    stack = [start_index - 1]
    color = [0] * length_dots
    result = []
    while stack:
        v = stack.pop(0)
        if color[v] == 0:
            result.append(v + 1)
            color[v] = 1
            stack.append(v)
            for number in vertex[v].split():
                if color[int(number) - 1] == 0:
                    stack.append(int(number) - 1)
    print(*result)



def main():
    line = sys.stdin.readline().rstrip().split()
    n = int(line[0])
    m = int(line[1])
    vertex = [''] * n
    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        vertex[int(line[0]) - 1] += line[1] + ' '
        vertex[int(line[1]) - 1] += line[0] + ' '
    dfs(3, n, vertex)


if __name__ == '__main__':
    main()

