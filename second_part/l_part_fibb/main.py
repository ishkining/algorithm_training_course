import sys


def find_fibb(number, division):
    if number <= 1:
        return 1
    return (find_fibb(number - 1, division) + find_fibb(number - 2, division)) % 10**division


def main():
    number, k = sys.stdin.readline().rstrip().split()
    print(find_fibb(int(number), int(k)))


if __name__ == '__main__':
    main()