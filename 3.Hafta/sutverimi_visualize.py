import pandas as pd
import matplotlib.pyplot as plt
import os

# Veriyi yükleme
dizin_yolu = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(dizin_yolu, 'data.csv')

try:
    df = pd.read_csv(dosya_yolu)
except FileNotFoundError:
    print(f"Hata: {dosya_yolu} bulunamadı. Lütfen önce sutverimi_data.py dosyasını çalıştırın.")
    exit(1)

# 1. Sıcaklık ve Süt Miktarı Arasındaki İlişki (Scatter Plot)
plt.figure(figsize=(8,6))
plt.scatter(df['Sicaklik'], df['Sut_Miktari'], alpha=0.6, color='dodgerblue')
plt.title('Sıcaklık ve Süt Miktarı İlişkisi')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Süt Miktarı (Litre)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(dizin_yolu, 'scatter_plot.png'))
plt.close()

# 2. Sıcaklık Dağılımı (Histogram)
plt.figure(figsize=(8,6))
plt.hist(df['Sicaklik'], bins=20, color='coral', edgecolor='black')
plt.title('Sıcaklık Dağılımı')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Frekans')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(dizin_yolu, 'sicaklik_hist.png'))
plt.close()

# 3. Süt Miktarı Dağılımı (Histogram)
plt.figure(figsize=(8,6))
plt.hist(df['Sut_Miktari'], bins=20, color='mediumseagreen', edgecolor='black')
plt.title('Süt Miktarı Dağılımı')
plt.xlabel('Süt Miktarı (Litre)')
plt.ylabel('Frekans')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(dizin_yolu, 'sut_miktari_hist.png'))
plt.close()

print("Grafikler (scatter_plot.png, sicaklik_hist.png, sut_miktari_hist.png) başarıyla oluşturuldu!")
