import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    nums1 = [int(number) for number in line.split(' ')]
    m = int(input())
    line = sys.stdin.readline().rstrip()
    nums2 = [int(number) for number in line.split(' ')]

    dp = [[0 for _ in range(len(n))] for _ in range(len(m))]
    max_segment = 0
    for i in range(len(m)):
        for j in range(len(n)):
            if nums2[i] == nums1[j]:
                if i > 0 and j > 0:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] += 1
                max_segment = max(max_segment, dp[i][j])

    print(max_segment)


if __name__ == '__main__':
    main()