import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/results.csv")

# Zaman grafiği
plt.figure()
plt.plot(df["N"], df["DP_time"], label="DP")
plt.plot(df["N"], df["GA_time"], label="GA")
plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Süre (saniye)")
plt.title("Zaman Karşılaştırması")
plt.legend()
plt.savefig("../results/runtime_graph.png")

# Doğruluk grafiği
plt.figure()
plt.plot(df["N"], df["DP_value"], label="DP")
plt.plot(df["N"], df["GA_value"], label="GA")
plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Toplam Değer")
plt.title("Sonuç Karşılaştırması")
plt.legend()
plt.savefig("../results/accuracy_graph.png")

print("Grafikler oluşturuldu.")