import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    array = [int(number) for number in line.split(' ')]
    for i in range(n):
        is_something_changed = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_something_changed = True

        if not is_something_changed:
            break
        print(array)


if __name__ == '__main__':
    main()
