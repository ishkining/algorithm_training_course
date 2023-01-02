import sys


def main():
    n = int(input())
    array = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip().split(' ')
        array.append((int(line[0]), int(line[1])))
    array.sort()
    for index in range(len(array) - 1):
        if array[index + 1][0] <= array[index][1]:
            array[index + 1] = (min(array[index][0], array[index + 1][0]), max(array[index][1], array[index + 1][1]))
            array[index] = None

    for element in array:
        if element:
            print(*element)


if __name__ == '__main__':
    main()