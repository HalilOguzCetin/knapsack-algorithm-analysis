import csv
import time
from dp_knapsack import knapsack_dp, read_data
from genetic_algorithm import genetic_algorithm

files = [
    ("50", "../data/data_50.csv"),
    ("200", "../data/data_200.csv"),
    ("1000", "../data/data_1000.csv"),
    ("5000", "../data/data_5000.csv"),
    ("10000", "../data/data_10000.csv")
]

capacity = 1000

with open("../results/results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "DP_value", "DP_time", "GA_value", "GA_time", "Accuracy_Gap"])

    for n, file in files:
        weights, values = read_data(file)

        print(f"{n} elemanlı veri seti çalıştırılıyor...")

        start = time.time()
        dp_val = knapsack_dp(weights, values, capacity)
        dp_time = time.time() - start

        start = time.time()
        ga_val = genetic_algorithm(weights, values, capacity)
        ga_time = time.time() - start

        accuracy_gap = abs(dp_val - ga_val) / dp_val * 100
        accuracy_gap = round(accuracy_gap, 2)

        writer.writerow([n, dp_val, dp_time, ga_val, ga_time, accuracy_gap])

print("Sonuçlar results.csv dosyasına yazıldı.")