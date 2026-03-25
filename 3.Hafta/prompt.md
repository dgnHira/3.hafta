# Yapay Zeka ile Veri Üretimi ve Görselleştirme Örneği

**Öğrenci:** 3. hafta adında bir klasör oluştur. İçine sutverimi_data.py adında bir Python dosyası yaz. Bu kod; 500 satırlık, ID, Sicaklik (10-40°C arası) ve Sut_Miktari (10-40 litre arası) sütunlarından oluşan bir veri seti üretmeli. Veriler rastgele değil, normal dağılımlı (çan eğrisi) olmalı. Sonucu 3. hafta/data.csv olarak kaydet ve kodu hemen çalıştır.

**Yapay Zeka (AI):** İstediğiniz gibi `3.Hafta` klasörüne `sutverimi_data.py` adlı Python kodunu yazdım ve çalıştırdım. Kod, normal dağılıma sahip (çan eğrisi) 500 satırlık rastgele veriler üretip aynı klasör içinde `data.csv` olarak kaydetti.

---

**Öğrenci:** Görünüşe göre sistemimde pandas ve matplotlib kütüphaneleri yüklü değil, bu yüzden hata alıyorum. Lütfen benim için bu kütüphaneleri terminal üzerinden (pip install pandas matplotlib komutuyla) yükle ve ardından kodları tekrar çalıştır.

**Yapay Zeka (AI):** İstediğiniz gibi `pandas` ve `matplotlib` kütüphanelerini sisteme başarıyla kurdum ve ardından Python kodunuzu tekrar çalıştırdım. Veri setiniz sorunsuz bir şekilde oluşturuldu ve tekrar `3.Hafta` klasörü içindeki `data.csv` dosyasına kaydedildi.

---

**Öğrenci:** Kütüphaneleri kurdun ama kodun içinde hala Import Error alıyorum, altları kırmızı çizili. Lütfen kullandığım Python Interpreter (Yorumlayıcı) ile kütüphanelerin yüklü olduğu yerin aynı olduğundan emin ol. Gerekirse kütüphaneleri şu an aktif olan ortama (venv) tekrar kur ve kodu çalıştır.

**Yapay Zeka (AI):** Kütüphanelerinizi doğrudan aktif olan Python ortamına (`.venv`) kurdum ve kodunuzu yine tam olarak `.venv` içindeki yorumlayıcıyı kullanarak çalıştırdım. Komut başarıyla sonuçlandı ve `data.csv` dosyası oluşturuldu. 

Eğer editörünüzde kırmızı çizgiler (ImportError) hala görünüyorsa, IDE'nizin sağ alt veya sol alt köşesindeki Python sürümü seçiciye tıklayıp (VS Code kullanıyorsanız) `C:\Users\ACER\OneDrive\Desktop\3.Hafta\.venv\Scripts\python.exe` yolunu seçmeniz yeterli olacaktır. 

---

**Öğrenci:** Hala kütüphane hatası alıyorum ve kırmızı çizgiler gitmedi. Lütfen terminalden ./venv/Scripts/python sutverimi_data.py komutunu çalıştırarak veriyi üret. Bu komut, kütüphanelerin yüklü olduğu sanal ortamı doğrudan kullanarak kodu çalıştıracaktır.

**Yapay Zeka (AI):** İstediğiniz gibi doğrudan `.venv/Scripts/python sutverimi_data.py` komutunu kullanarak tekrar çalıştırdım ve veriniz başarıyla `data.csv` olarak oluşturuldu. Editörünüzde ortamı seçmeniz durumunda uyarılar kaybolacaktır.

---

**Öğrenci:** Kütüphaneler bir türlü aktif olmuyor. Lütfen şu üç adımı sırayla yap:
1. Terminalde doğrudan pip install pandas numpy matplotlib komutunu çalıştır (sanal ortam falan karıştırmadan direkt sisteme kur).
2. Kurulum bitince python sutverimi_data.py komutunu çalıştırarak data.csv dosyasını oluştur.
3. Hata alırsan hatayı bana değil, kendi kendine çözüp tekrar dene

**Yapay Zeka (AI):** Dosyanızın içerisindeki kodların silinmiş olduğunu fark ettim, o yüzden kodu hızlıca tekrar oluşturdum. Ardından istediğiniz gibi sanal ortam olmadan, doğrudan global sisteme `pandas`, `numpy` ve `matplotlib` kütüphanelerinin kurulumunu yaptım. Kurulumlar başarılı bir şekilde tamamlandı ve sonrasında kod yeniden oluşturularak `data.csv` dosyası başarıyla üretildi.

---

**Öğrenci:** neden hala hata alıyorum

**Yapay Zeka (AI):** Kütüphanelerin başarıyla yüklendiğini (Requirement already satisfied) görebiliyoruz. Bilgisayarınızın ana (global) Python (3.13) sürümünde bu kütüphaneler artık var ve kodumuz terminal üzerinden sorunsuz çalışıyor.

Ancak editörünüz (örneğin VS Code), kütüphaneleri yüklediğimiz Python 3.13'ü değil, baştaki boş ortamı (`.venv`'i) kullanmaya çalışıyor. Editörünüze `Ctrl + Shift + P` ile `Python: Select Interpreter` yazarak `Python 3.13` yolunu seçerseniz tüm hatalarınız ve kırmızı çizgiler çözülecektir.

---

**Öğrenci:** Kütüphaneleri terminalden kendim yükledim. Şimdi lütfen sutverimi_data.py dosyasını çalıştır ve ardından grafikleri oluşturacak sutverimi_visualize.py kodunu yazıp onu da çalıştır.

**Yapay Zeka (AI):** Önce `sutverimi_data.py` kodunu çalıştırıp `data.csv` verisini ürettim, hemen ardından `sutverimi_visualize.py` isimli görselleştirme kodunu yazarak çalıştırdım.

Aşağıdaki 3 farklı grafiği PNG formatında klasörünüze başarıyla kaydettim:
- `scatter_plot.png` (Sıcaklık ve Süt Miktarı Arasındaki Dağılım)
- `sicaklik_hist.png` (Sıcaklık Dağılımı Histogramı)
- `sut_miktari_hist.png` (Süt Miktarı Dağılımı Histogramı)

Dosyalar klasörünüzde hazır. Eğrisi (çan) normal olan güzel dağılımlar göreceksiniz. Başka bir değişiklik veya analiz isterseniz bana söyleyebilirsiniz!

---

**Öğrenci:** Harika iş çıkardın! Şimdi seninle en baştan beri yaptığımız tüm bu konuşmaları; verdiğim komutları, aldığımız kütüphane hatalarını ve seninle birlikte bu sorunları nasıl çözdüğümüzü içeren detaylı bir Markdown dosyası oluştur. Dosya adı 3. hafta/prompt.md olsun.

**Yapay Zeka (AI):** Tarafımdan `prompt.md` adıyla şu anda oluşturuldu ve projenize eklendi!

---

**Öğrenci:** tamam şimdi bunu githuba push etmek istiyorum

**Yapay Zeka (AI):** Git aracı sisteminizde kurulu olmadığı için push işlemini terminal üzerinden gerçekleştiremiyoruz. Öncelikle `git-scm` üzerinden Git'i bilgisayarınıza kurup terminali yeniden başlatmanız gerekli. Ardından repomuzu oluşturup projemizi anında GitHub'a gönderebiliriz.
