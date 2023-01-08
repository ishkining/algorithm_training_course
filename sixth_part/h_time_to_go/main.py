import sys


def dfs(start_index, vertex):
    stack = [start_index - 1]
    color = [0] * len(vertex)
    result = [[None, None] for _ in range(len(vertex))]

    counter = 0
    print(vertex)
    print(result)
    while stack:
        print(stack)
        v = stack.pop(0)
        if not result[v][0] or not result[v][1]:
            if result[v][0] and not result[v][1]:
                result[v][1] = counter
            else:
                if not result[v][0]:
                    result[v][0] = counter
                    print('heloo', result)

                if len(vertex[v]) == 0:
                    counter += 1
                    result[v][1] = counter
                else:
                    for index in range(len(vertex[v]) + 1):
                        if index == len(vertex[v]):
                            stack.insert(index, v)
                        elif not result[vertex[v][index]][0] or not result[vertex[v][index]][1]:
                            stack.insert(index, vertex[v][index])
            counter += 1

        print(counter)
    print(*result)


def main():
    line = sys.stdin.readline().rstrip().split()
    n = int(line[0])
    m = int(line[1])
    vertex = [[] for _ in range(n)]
    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        vertex[int(line[0]) - 1].append(int(line[1]) - 1)
    for index in range(n):
        vertex[index].sort()
    dfs(1, vertex)


if __name__ == '__main__':
    main()

