import pandas as pd
import numpy as np
import os

n = 500

# Normal dağılımlı üretim
sicaklik = np.random.normal(loc=25, scale=5, size=n)
sicaklik = np.clip(sicaklik, 10, 40)

sut_miktari = np.random.normal(loc=25, scale=5, size=n)
sut_miktari = np.clip(sut_miktari, 10, 40)

# Veriyi DataFrame'e dönüştürme
df = pd.DataFrame({
    'ID': range(1, n + 1),
    'Sicaklik': np.round(sicaklik, 2),
    'Sut_Miktari': np.round(sut_miktari, 2)
})

# Dosyanın bulunduğu dizini dinamik alma ve data.csv olarak kaydetme
dizin_yolu = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(dizin_yolu, 'data.csv')

df.to_csv(dosya_yolu, index=False)
print(f"Veri seti başarıyla oluşturuldu ve şuraya kaydedildi: {dosya_yolu}")
