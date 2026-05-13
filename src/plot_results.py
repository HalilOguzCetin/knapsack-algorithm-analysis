import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/results.csv")

# X eksenini düzgün göstermek için string yap
df["N"] = df["N"].astype(str)

# Zaman grafiği
plt.figure()
plt.plot(df["N"], df["DP_time"], marker="o", label="DP")
plt.plot(df["N"], df["GA_time"], marker="o", label="GA")
plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Süre (saniye)")
plt.title("Zaman Karşılaştırması")
plt.legend()
plt.grid()
plt.savefig("../results/runtime_graph.png")

# Doğruluk grafiği
plt.figure()
plt.plot(df["N"], df["DP_value"], marker="o", label="DP")
plt.plot(df["N"], df["GA_value"], marker="o", label="GA")
plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Toplam Değer")
plt.title("Sonuç Karşılaştırması")
plt.legend()
plt.grid()
plt.savefig("../results/accuracy_graph.png")

print("Grafikler oluşturuldu.")