import sys


def main():
    flower_counter = {'0': 0, '1': 0, '2': 0}
    n = int(input())
    line = sys.stdin.readline().rstrip().split(' ')
    for number in line:
        flower_counter[number] += 1

    print(flower_counter['0'] * '0 ' + flower_counter['1'] * '1 ' + flower_counter['2'] * '2 ')


if __name__ == '__main__':
    main()
