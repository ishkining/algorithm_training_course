def main():
    num_lines = int(input())
    array_lines = []
    lines = input().split(' ')
    for index in range(num_lines): # sort line[index]
        array_lines.append((''.join(list(sorted(char for char in lines[index]))), index))

    array_lines = list(sorted(array_lines, key=lambda inner_tuple: inner_tuple[0], reverse=True))
    result = [[] for _ in range(len(array_lines))]
    counter = 0
    print(array_lines)
    while len(array_lines) > 0:
        print(array_lines, ' ', counter)
        collapsed_tuple = array_lines.pop(0)
        result[counter].append(collapsed_tuple[1])
        if len(array_lines) <= 0:
            continue
        if collapsed_tuple[0] != array_lines[0][0]:
            counter += 1

    for array in result:
        if array:
            print(*array)


if __name__ == '__main__':
    main()
