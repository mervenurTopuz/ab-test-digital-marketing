import pandas as pd
import numpy as np

# Rastgeleliğin her seferinde aynı sonuçları vermesi için
np.random.seed(42)
n_samples = 2000 # 2000 kişilik bir kullanıcı trafiği oluşturuyoruz

# 1. Kullanıcı ID'leri ve Test Grupları (A: Mevcut Tasarım, B: Yeni Tasarım)
kullanici_id = range(10001, 10001 + n_samples)
grup = np.random.choice(['A_Kontrol', 'B_Test'], size=n_samples, p=[0.5, 0.5])

# 2. Boş bir tablo (DataFrame) oluşturuyoruz
df = pd.DataFrame({'Kullanici_ID': kullanici_id, 'Test_Grubu': grup})

# 3. Cihaz kullanımı ve Sitede Geçirilen Süre (Saniye)
df['Cihaz'] = np.random.choice(['Mobil', 'Masaustu'], size=n_samples, p=[0.7, 0.3])
df['Sitede_Gecirilen_Sure_Sn'] = np.random.randint(10, 300, size=n_samples)

# 4. A/B Testi Dönüşüm (Satın Alma) Davranışı
# Gerçekçi olması için B Grubuna (yeni tasarıma) %14, A grubuna %8 satın alma ihtimali veriyoruz.
satin_alma = []
for g in df['Test_Grubu']:
    if g == 'A_Kontrol':
        satin_alma.append(np.random.choice([0, 1], p=[0.92, 0.08])) # 1: Satın aldı, 0: Almadı
    else:
        satin_alma.append(np.random.choice([0, 1], p=[0.86, 0.14]))

df['Satin_Alma'] = satin_alma

# 5. Veriyi bilgisayara CSV formatında kaydediyoruz
df.to_csv('dijital_pazarlama_ab_test.csv', index=False)

# Ekrana kontrol için çıktı verelim
print("--- A/B Testi Veri Seti İlk 5 Satır ---")
print(df.head())
print("\nVeri başarıyla 'dijital_pazarlama_ab_test.csv' adıyla kaydedildi!")
