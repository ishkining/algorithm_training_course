import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    lines_array = [int(number) for number in line.split(' ')]
    lines_array.sort(reverse=True)
    for index in range(len(lines_array) - 2):
        if lines_array[index] < lines_array[index + 1] + lines_array[index + 2]:
            print(lines_array[index] + lines_array[index + 1] + lines_array[index + 2])
            break


if __name__ == '__main__':
    main()