import pandas as pd
from scipy.stats import chi2_contingency

# 1. Veriyi okuma
df = pd.read_csv('dijital_pazarlama_ab_test.csv')

# 2. Çapraz Tablo Oluşturma (Hangi gruptan kaç kişi aldı/almadı)
crosstab = pd.crosstab(df['Test_Grubu'], df['Satin_Alma'])
print("--- Grup ve Satın Alma Çapraz Tablosu ---")
print(crosstab)
print("\nİstatistiksel Test Yapılıyor...\n")

# 3. Ki-Kare (Chi-Square) Testi Uygulama
# Bu test bize bir 'P-Değeri' (p-value) verecek. 
stat, p_value, dof, expected = chi2_contingency(crosstab)

print(f"P-Değeri (P-Value): {p_value:.5f}\n")

# 4. Sonucu Yorumlama (Karar Destek)
alpha = 0.05 # Anlamlılık düzeyi (%5 yanılma payı kabul ediyoruz)

print("--- 🎯 A/B TESTİ KARARI ---")
if p_value < alpha:
    print("🎉 Sonuç: Aradaki fark İSTATİSTİKSEL OLARAK ANLAMLI!")
    print("Yorum: B Grubu (Yeni Tasarım) tesadüf eseri değil, gerçekten daha başarılı.")
    print("Aksiyon: Yeni tasarım tüm müşteriler için canlıya alınabilir.")
else:
    print("⚠️ Sonuç: Aradaki fark tesadüfi olabilir. Anlamlı bir fark YOK.")
    print("Yorum: Yeni tasarımın kesin bir üstünlüğü kanıtlanamadı.")
    print("Aksiyon: Eski tasarımda kalınmalı veya test süresi uzatılmalı.")
