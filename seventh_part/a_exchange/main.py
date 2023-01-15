import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip().split()
    list_exchange = [int(value) for value in line]
    result = 0
    for index in range(len(list_exchange) - 1):
        if list_exchange[index] < list_exchange[index + 1]:
            result += list_exchange[index + 1] - list_exchange[index]

    print(result)


if __name__ == '__main__':
    main()