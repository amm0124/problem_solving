import sys
import math

def fold_file(t, k_values, files_list):
    for idx in range(t):
        k = k_values[idx]
        file = files_list[idx]
        dp = [[math.inf] * (k + 1) for _ in range(k + 1)]
        partial_sum = [0] * (k + 1)

        for i in range(1, k + 1):
            dp[i][i] = 0

        for i in range(k):
            partial_sum[i + 1] = partial_sum[i] + file[i]

        for length in range(2, k + 1):
            for start in range(1, k - length + 2):
                end = start + length - 1
                for i in range(start, end):
                    dp[start][end] = min(
                        dp[start][end],
                        dp[start][i] + dp[i + 1][end] + partial_sum[end] - partial_sum[start - 1]
                    )

        print(dp[1][k])

if __name__ == "__main__":
    t = int(input())
    k_values = []
    files_list = []

    for _ in range(t):
        k = int(input())
        k_values.append(k)
        files = list(map(int, input().split()))
        files_list.append(files)

    fold_file(t, k_values, files_list)
