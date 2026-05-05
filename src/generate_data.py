import random
import csv

def generate_knapsack_data(n, filename):
    weights = [random.randint(1, 50) for _ in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["weight", "value"])
        
        for w, v in zip(weights, values):
            writer.writerow([w, v])

    print(f"{n} elemanlı veri üretildi -> {filename}")


if __name__ == "__main__":
    generate_knapsack_data(50, "../data/data_50.csv")
    generate_knapsack_data(200, "../data/data_200.csv")
    generate_knapsack_data(1000, "../data/data_1000.csv")
