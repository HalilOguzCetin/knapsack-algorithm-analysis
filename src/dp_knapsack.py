import csv
import time

def read_data(filename):
    weights = []
    values = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            weights.append(int(row['weight']))
            values.append(int(row['value']))

    return weights, values


def knapsack_dp(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    files = [
        "../data/data_50.csv",
        "../data/data_200.csv",
        "../data/data_1000.csv",
        "../data/data_5000.csv",
        "../data/data_10000.csv"
    ]

    capacity = 1000

    for file in files:
        weights, values = read_data(file)

        start = time.time()
        result = knapsack_dp(weights, values, capacity)
        end = time.time()

        print(f"{file} -> max değer: {result}, süre: {end - start:.5f} saniye")