import sys


def dfs(start_index, vertex):
    stack = [start_index - 1]
    color = [0 for _ in range(len(vertex))]
    while stack:
        popped_element = stack.pop(0)
        if color[popped_element] == 0:
            color[popped_element] = 1
            for element in vertex[popped_element].split():
                if color[int(element) - 1] == 0:
                    stack.append(int(element) - 1)
    return ' '.join([str(index + 1) for index in range(len(color)) if color[index] == 1]), \
                    [index for index in range(len(color)) if color[index] == 1]


def main():
    line = sys.stdin.readline().rstrip().split()
    n = int(line[0])
    m = int(line[1])
    vertex = ['' for _ in range(n)]
    for _ in range(m):
        line = sys.stdin.readline().rstrip().split()
        vertex[int(line[0]) - 1] = line[1] + ' '
        vertex[int(line[1]) - 1] = line[0] + ' '

    result = []
    used = []
    for index in range(n):
        if index not in used:
            new_result, new_used = dfs(index, vertex)
            result.append(dfs(index, vertex))
            used += [element for element in new_used if element not in used]
            print(new_result)


if __name__ == '__main__':
    main()
