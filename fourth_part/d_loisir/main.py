import sys


def main():
    n = int(input())
    our_set = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        if line not in our_set:
            our_set.append(line)

    for element in our_set:
        print(element)


if __name__ == '__main__':
    main()