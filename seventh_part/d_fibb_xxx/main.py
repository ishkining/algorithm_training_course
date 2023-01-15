def main():
    n = int(input())
    dp = [1, 1, 2] + [0] * (n - 2)
    for index in range(3, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    print(dp[n])


if __name__ == '__main__':
    main()