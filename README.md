# Kırklareli Toplu Taşıma Planlama – Softmax Tabanlı Karar Desteği

Bu proje, Kırklareli'nin **Karakaş**, **İstasyon** ve **Karacaibrahim** mahalleleri için yeni bir toplu taşıma güzergahının belirlenmesi amacıyla **Softmax algoritmasına** dayalı bir karar destek sistemi geliştirir.

##  Proje Amacı
Farklı kriterleri (nüfus yoğunluğu, mevcut ulaşım altyapısı, maliyet analizi, çevresel etki, sosyal fayda) değerlendirerek en uygun güzergahı bilimsel olarak belirlemektir.

---

## Kullanılan Bileşenler

| Bileşen | Açıklama |
|--------|----------|
| `numpy` | Sayısal işlemler ve matris hesaplamaları |
| `pandas` | Veri çerçevesi (DataFrame) yapısı |
| `scipy.special.softmax` | Softmax normalizasyonu |
| `matplotlib` | Grafiksel görselleştirme (maliyet-fayda analizi) |

---

##  Softmax Algoritması
Softmax, kriter bazında mahalleleri normalize eder. Daha yüksek değere sahip olan kriterler karar puanını daha fazla etkiler.

Her mahalle için toplam skor:  
 `Toplam Skor = Softmax(Kriter Skorları) ⨉ Kriter Ağırlıkları`

Ayrıca maliyet-fayda dengesi de ayrı bir analizde değerlendirilir.

---

## Çıktılar
- **En uygun mahalle** belirlenir.
- **Grafiksel analiz** ile net fayda skorları görselleştirilir.
- **Konsol çıktısı** olarak sıralı karar listesi sunulur.

---

##  Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri kur:
    ```bash
    pip install numpy pandas matplotlib scipy
    ```

2. Python dosyasını çalıştır:
    ```bash
    python kirklareli_toplu_tasima_softmax.py
    ```

---

##  Dosya Yapısı
```
kirklareli_toplu_tasima_softmax/
├── softmax.py       # Softmax algoritmasını uygulayan Python kodu
├── sonuc_grafik.png            # Sonuçları gösteren grafik (otomatik oluşur)
└── README.md                   # Proje tanıtım dosyası
```
##  Geliştirici
- **Ad Soyad:** [Ceren Öztürk]
- **Katkı:** Projenin tüm aşamalarını tek başına gerçekleştirmiştir.
