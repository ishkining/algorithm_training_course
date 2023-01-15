import sys


def main():
    line = sys.stdin.readline().rstrip().split()
    n, k = int(line[0]) - 1, int(line[1])
    ways_jumping = [0, 1] + [0] * (n - 1)
    for index in range(2, n + 1):
        times = 0
        if k >= index:
            ways_jumping[index] += 1
        while index - times > 0 and k > times:
            times += 1
            ways_jumping[index] += ways_jumping[index - times]
    print(ways_jumping)


if __name__ == '__main__':
    main()