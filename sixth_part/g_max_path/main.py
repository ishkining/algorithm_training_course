import sys


def bfs(start_index: int, vertexes: list) -> list:
    vertex_met = [0] * len(vertexes)
    queue = [start_index - 1]
    path = [0] * len(vertexes)
    while queue:
        v = queue.pop()
        if vertex_met[v] == 0:
            vertex_met[v] = 1
            for element in vertexes[v].split():
                index = int(element) - 1
                if vertex_met[index] == 0:
                    queue.insert(0, index)
                    path[index] = path[v] + 1
    return max(path)


def main():
    line = sys.stdin.readline().rstrip().split()
    n = int(line[0])
    m = int(line[1])
    vertexes = [''] * n

    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        vertexes[int(line[0]) - 1] += line[1] + ' '
        vertexes[int(line[1]) - 1] += line[0] + ' '
    line = sys.stdin.readline().rstrip().split()
    start_index = int(line[0])
    result = bfs(start_index, vertexes)
    print(result)


if __name__ == '__main__':
    main()
