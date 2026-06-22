# ab-test-digital-marketing
# 📈 Dijital Pazarlama A/B Testi ve Dönüşüm Oranı Analizi

Bu proje, bir e-ticaret platformunda iki farklı web sitesi tasarımının (A/B Testi) müşteri dönüşüm oranları (satın alma) üzerindeki etkisini istatistiksel olarak ölçmek amacıyla gerçekleştirilmiştir.

## 📌 Proje Amacı ve İş Problemi
Pazarlama stratejilerinde veriye dayalı karar vermek (data-driven decision making) hayati önem taşır. Bu projede:
* Rastgele seçilen 2000 kullanıcılık bir trafik verisi üzerinde, eski tasarım (A Grubu) ile yeni tasarımın (B Grubu) performansları karşılaştırılmıştır.
* Kullanıcıların cihaz tipleri ve sitede geçirdikleri süreler analiz edilmiştir.
* İki grup arasındaki dönüşüm oranı farkının tesadüfi olup olmadığını kanıtlamak için istatistiksel hipotez testi uygulanmıştır.

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python
* **Veri Manipülasyonu:** Pandas, NumPy
* **İstatistiksel Analiz:** SciPy (Chi-Square / Ki-Kare Testi)
* **Veri Görselleştirme:** Matplotlib, Seaborn

## 🚀 Analiz Sonuçları ve İş Kararı (Karar Destek)
Yapılan veri keşfi (EDA) sonucunda B Grubunun (yeni tasarım) daha yüksek bir satın alma oranı yakaladığı gözlemlenmiştir. Bu farkın bilimsel geçerliliğini kanıtlamak için **Ki-Kare (Chi-Square) Hipotez Testi** uygulanmıştır.

* **P-Değeri (P-Value):** 0.0000
* **Anlamlılık Düzeyi (Alpha):** 0.05

**Analitik Yorum ve Aksiyon:** Hesaplanan P-Değeri 0.05'ten küçük olduğu için iki tasarım arasındaki farkın **istatistiksel olarak anlamlı** olduğu kanıtlanmıştır. Yeni tasarımın başarısı tesadüf değildir. İş birimlerine (Pazarlama ve Ürün Yönetimi) yeni tasarımın tüm müşteriler için yayına alınması (roll-out) raporlanmıştır.

## 📂 Proje Adımları
1. **Veri Üretimi (`ab_test_veri.py`):** 2000 satırlık dijital pazarlama tıklama (clickstream) ve dönüşüm verisi oluşturuldu.
2. **Görselleştirme (`ab_gorsellestirme.py`):** Grupların dönüşüm oranları ve sitede geçirilen süre dağılımları grafiklere döküldü.
3. **Hipotez Testi (`ab_testi_sonuc.py`):** Çapraz tablolar (crosstab) oluşturularak Ki-Kare testi yapıldı ve veri destekli nihai iş kararı verildi.
