# Süt Verimi ve Sıcaklık Analizi (Hafta 3)

## Veri Seti Kurgusu
Bu çalışma, çevresel faktörlerin (sıcaklık) hayvansal üretim (süt miktarı) üzerindeki etkisini simüle etmek amacıyla hazırlanmıştır.

## Değişken Detayları

### Sicaklik (°C):
- **Birim:** Santigrat Derece
- **Dağılım:** Normal Dağılım (Ortalama 25°C)
- **Açıklama:** Hayvanların bulunduğu barınak sıcaklığını temsil eder.

### Sut_Miktari (Litre):
- **Birim:** Litre
- **Dağılım:** Normal Dağılım (Ortalama 25 Litre)
- **Açıklama:** İlgili sıcaklık değerinde alınan günlük toplam süt miktarını temsil eder.

## Kullanılan Yöntem
Veri seti, Python'un Numpy kütüphanesi kullanılarak Normal Dağılım (Gaussian Distribution) prensibine göre üretilmiştir. Bu yöntemle verilerin gerçek hayattaki gibi uç değerlerden ziyade ortalamada yoğunlaşması sağlanmıştır. Görselleştirme aşamasında Matplotlib kütüphanesi ile dağılım grafikleri (Histogram) oluşturulmuştur.
