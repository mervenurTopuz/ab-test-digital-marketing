import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi okuma
df = pd.read_csv('dijital_pazarlama_ab_test.csv')

print("Veri başarıyla yüklendi! Hesaplamalar yapılıyor...\n")

# Grupların Dönüşüm (Satın Alma) Oranlarını Hesaplama (Yüzde olarak)
cr_rates = df.groupby('Test_Grubu')['Satin_Alma'].mean() * 100
print("--- Gruplara Göre Dönüşüm (Satın Alma) Oranları ---")
print(cr_rates)
print("\nLütfen açılan grafik penceresini inceledikten sonra kapatın.")
print("Bir pencereyi kapatmadan diğer grafik açılmaz!\n")

# Grafiklerin genel temasını ayarlayalım
sns.set_theme(style="whitegrid")

# 2. Grafik 1: A ve B Grubunun Dönüşüm Oranları (Bar Plot)
plt.figure(figsize=(6, 4))
# Not: Önceki projede aldığımız kırmızı uyarıyı (FutureWarning) almamak için kodu güncelledim :)
sns.barplot(x=cr_rates.index, y=cr_rates.values, hue=cr_rates.index, palette='viridis', legend=False)
plt.title('A ve B Grubunun Dönüşüm (Satın Alma) Oranları (%)')
plt.ylabel('Dönüşüm Oranı (%)')
plt.xlabel('Test Grubu')
plt.show()

# 3. Grafik 2: Cihaza (Mobil/Masaüstü) Göre Sitede Geçirilen Süre (Kutu Grafiği)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Cihaz', y='Sitede_Gecirilen_Sure_Sn', hue='Test_Grubu', palette='Set2')
plt.title('Cihaza ve Test Grubuna Göre Sitede Geçirilen Süre')
plt.ylabel('Sitede Geçirilen Süre (Saniye)')
plt.show()

print("Tüm grafikler başarıyla çizdirildi! İstatistiksel test aşamasına geçmeye hazırız.")
