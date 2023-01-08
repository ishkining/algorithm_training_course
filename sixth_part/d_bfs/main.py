import sys


def bfs(start_index: int, vertexes: list, length: int) -> list:
    vertex_met = [0] * length
    queue = [start_index - 1]
    result = []
    while queue:
        v = queue.pop()
        if vertex_met[v] == 0:
            vertex_met[v] = 1
            for element in vertexes[v].split():
                index = int(element) - 1
                if vertex_met[index] == 0:
                    queue.insert(0, index)
            result.append(v + 1)
    return result


def main():
    line = sys.stdin.readline().rstrip().split()
    n = int(line[0])
    m = int(line[1])
    vertexes = [''] * n

    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        vertexes[int(line[0]) - 1] += line[1] + ' '
        vertexes[int(line[1]) - 1] += line[0] + ' '

    result = bfs(3, vertexes, n)
    print(*result)


if __name__ == '__main__':
    main()
