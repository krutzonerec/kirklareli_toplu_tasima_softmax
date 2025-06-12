# Kırklareli Mahalleleri için Toplu Taşıma Hattı Planlama (Softmax)

import numpy as np
import pandas as pd
from scipy.special import softmax
import matplotlib.pyplot as plt


neighborhoods = ["Karakaş", "İstasyon", "Karacaibrahim"]

criteria = ["Nüfus Yoğunluğu", "Ulaşım Altyapısı", "Maliyet", "Çevresel Etki", "Sosyal Fayda"]

data = np.array([
    [8, 6, 4, 7, 9],   # Karakaş
    [5, 8, 6, 6, 7],   # İstasyon
    [7, 5, 5, 8, 6]    # Karacaibrahim
])

weights = np.array([0.25, 0.2, 0.15, 0.2, 0.2])

print("Kriter Ağırlıkları:")
for crit, w in zip(criteria, weights):
    print(f"{crit}: {w:.2f}")

softmax_scores = np.zeros_like(data, dtype=float)
for i in range(data.shape[1]):
    exp_scores = np.exp(data[:, i] - np.max(data[:, i]))
    softmax_scores[:, i] = exp_scores / np.sum(exp_scores)

weighted_scores = softmax_scores @ weights

score_df = pd.DataFrame(softmax_scores, columns=criteria)
score_df.insert(0, "Mahalle", neighborhoods)
score_df["Toplam Skor"] = weighted_scores

result_df = score_df.sort_values(by="Toplam Skor", ascending=False)

print("\nSoftmax Normalizasyonu Sonrası Kriter Bazlı Skorlar:")
print(score_df.round(3).to_string(index=False))

print("\nToplu Taşıma Hattı İçin Mahalle Önceliklendirmesi (Softmax Skoruna Göre):")
print(result_df[["Mahalle", "Toplam Skor"]].round(3).to_string(index=False))

benefit_weights = weights[[0, 1, 3, 4]]
cost_weight = weights[2]

benefit_score = softmax_scores[:, [0, 1, 3, 4]] @ benefit_weights
cost_score = softmax_scores[:, 2] * cost_weight
net_benefit = benefit_score - cost_score

mfa_df = pd.DataFrame({
    "Mahalle": neighborhoods,
    "Net Fayda Skoru": net_benefit
}).sort_values(by="Net Fayda Skoru", ascending=False)

print("\nMaliyet-Fayda Analizi Sonucu:")
print(mfa_df.to_string(index=False))

plt.figure(figsize=(8, 5))
plt.bar(mfa_df["Mahalle"], mfa_df["Net Fayda Skoru"], color='skyblue')
plt.title("Mahalle Bazlı Net Fayda Skoru")
plt.ylabel("Skor")
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
