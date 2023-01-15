import sys


def main():
    m = int(input())
    n = int(input())
    list_piles = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip().split()
        list_piles.append((int(line[0]), int(line[1])))
    list_piles.sort(reverse=True)

    result = 0
    for pile in list_piles:
        if m - pile[1] >= 0:
            result += pile[1] * pile[0]
            m -= pile[1]
        else:
            result += m * pile[0]
            break
    print(result)


if __name__ == '__main__':
    main()