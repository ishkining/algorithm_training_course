import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip().split(' ')
    line = list(sorted(line, key=lambda word: word, reverse=True))
    print(''.join(line))


if __name__ == '__main__':
    main()