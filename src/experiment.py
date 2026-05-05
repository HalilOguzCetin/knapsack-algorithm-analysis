import csv
import time
from dp_knapsack import knapsack_dp, read_data
from genetic_algorithm import genetic_algorithm

files = [
    ("50", "../data/data_50.csv"),
    ("200", "../data/data_200.csv"),
    ("1000", "../data/data_1000.csv")
]

capacity = 200

with open("../results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "DP_value", "DP_time", "GA_value", "GA_time"])

    for n, file in files:
        weights, values = read_data(file)

        # DP
        start = time.time()
        dp_val = knapsack_dp(weights, values, capacity)
        dp_time = time.time() - start

        # GA
        start = time.time()
        ga_val = genetic_algorithm(weights, values, capacity)
        ga_time = time.time() - start

        writer.writerow([n, dp_val, dp_time, ga_val, ga_time])

print("Sonuçlar results.csv dosyasına yazıldı.")