import pandas as pd
import matplotlib.pyplot as plt

# CSV oku
df = pd.read_csv("../results/results.csv")

# X ekseni düzgün görünsün
df["N"] = df["N"].astype(str)

# -------------------------
# 1) ZAMAN GRAFİĞİ
# -------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["N"],
    df["DP_time"],
    marker="o",
    label="DP"
)

plt.plot(
    df["N"],
    df["GA_time"],
    marker="o",
    label="GA"
)

plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Süre (saniye)")
plt.title("Zaman Karşılaştırması")

plt.legend()
plt.grid()

plt.savefig(
    "../results/runtime_graph.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -------------------------
# 2) SONUÇ GRAFİĞİ
# -------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["N"],
    df["DP_value"],
    marker="o",
    label="DP"
)

plt.plot(
    df["N"],
    df["GA_value"],
    marker="o",
    label="GA"
)

plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Toplam Değer")
plt.title("Sonuç Karşılaştırması")

plt.legend()
plt.grid()
plt.yscale("log")

plt.savefig(
    "../results/accuracy_graph.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -------------------------
# 3) SAPMA GRAFİĞİ
# -------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["N"],
    df["Accuracy_Gap"],
    marker="o"
)

plt.xlabel("Veri Boyutu (N)")
plt.ylabel("Sapma (%)")
plt.title("GA Sapma Oranı")

plt.grid()


plt.savefig(
    "../results/gap_graph.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("✓ runtime_graph.png oluşturuldu")
print("✓ accuracy_graph.png oluşturuldu")
print("✓ gap_graph.png oluşturuldu")
print("✓ Tüm grafikler hazır")