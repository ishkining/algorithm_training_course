import sys


def main():
    number_a = int(input())
    number_m = int(input())
    full_line = input()
    hash_array = [[0] * (2 + multiplier) for multiplier in range(len(full_line))]
    for i in range(len(full_line)):
        for j in range(i, -1, -1):
            hash_array[i][j + 1] = (ord(full_line[j]) * number_a ** (i-j)) + hash_array[i][j]
    print(hash_array)
    num_strs = int(input())
    for _ in range(num_strs):
        line = sys.stdin.readline().rstrip().split(' ')
        print((hash_array[int(line[1]) - 1][int(line[0])]) % number_m)


if __name__ == '__main__':
    main()