# 3. Hafta - Veri Üretimi ve Karşılaşılan Sorunların Çözüm Süreci

Bu belge, "3. Hafta" klasörü içerisinde yürütülen süt verimi veri seti oluşturma projesi boyunca verilen komutların, karşılaşılan ortam/kütüphane hatalarının ve bunlara yönelik üretilen çözüm adımlarının kapsamlı bir özetini içerir.

## 1. İlk İstek: Normal Dağılımlı Süt Verimi Verisi Üretmek
**Problem/Talep:** Kullanıcı, 500 satırdan oluşan, içinde `ID`, `Sicaklik` (10-40°C) ve `Sut_Miktari` (10-40 litre) sütunlarını barındıran; ancak verilerin tamamen rastgele olmadığı (çan eğrisi, normal dağılımlı) bir Python kodu (`sutverimi_data.py`) yazılmasını istedi.
**Çözüm:** `numpy.random.normal` kullanılarak ortalaması 25, standart sapması 5 olan normal dağılımlı bir veri seti oluşturuldu. Nadir uç değerler (10-40 dışı) `np.clip` ile sınırlandırılarak `data.csv` dosyasına başarıyla kaydedildi.

## 2. "ModuleNotFoundError" ve İlk Pip Kurulumu
**Problem:** Kullanıcının bilgisayarında `pandas` ve `matplotlib` kurulu olmadığı için çalıştırılan kod hata verdi.
**Çözüm:** Terminale doğrudan müdahale edilerek `pip install pandas matplotlib` komutu çalıştırıldı. Kurulum sonrası kod tekrar çalıştırılarak `data.csv` başarıyla elde edildi.

## 3. IDE ve Sanal Ortam (.venv) Çakışması
**Problem:** Kütüphaneler kurulmasına rağmen kullanıcının kod editöründe kelimelerin altı kırmızı çizili kalıyor (`ImportError` uyarısı veriyordu). Kullanıcı, kurulumları `.venv` adlı sanal ortama yapmamızı ve oradan çalıştırmamızı istedi.
**Çözüm:** `.\.venv\Scripts\python -m pip install` komutu kullanılarak kütüphaneler sanal ortama da dahil edildi ve kod doğrudan sanal ortam yorumlayıcısıyla (`.\.venv\Scripts\python sutverimi_data.py`) başarılı şekilde koşturuldu.

## 4. Kodun Silinmesi ve Global Python Çözümü
**Problem:** Ortam uyuşmazlığı can sıkmaya devam edince kullanıcı, sanal ortamları devre dışı bırakarak kütüphanelerin doğrudan bilgisayarın ana (global) Python sürümüne kurulmasını istedi(`pip install pandas numpy matplotlib`). Bu esnada `sutverimi_data.py` içerisindeki kodlar kullanıcı tarafından silinmişti.
**Çözüm:** Silinen veri seti kodu sıfırdan tekrar yazıldı, terminalden doğrudan sisteme kütüphane kurulumları tekrar yapıldı ve kod sorunsuzca çalışarak veriyi baştan üretti.

## 5. IDE Kırmızı Çizgi Hatalarının Nihai Analizi ve Çözümü
**Problem:** Her şey terminalde kusursuz çalışıp veriyi ortaya çıkartmasına rağmen kullanıcı "Neden hâlâ ekranda hata (kırmızı uyarılar) alıyorum?" diye sordu.
**Çözüm:** Kurulumların bilgisayarın `Python 3.13` global sürümüne yapıldığı; fakat VS Code editörünün inatla içi boş olan başka bir ortama (`.venv`) bakmaya devam ettiği tespit edildi. Kullanıcıya şu yönergeler verildi:
  - Editörde `Ctrl + Shift + P` tuşlarına basın.
  - `Python: Select Interpreter` (Yorumlayıcı Seç) adımına tıklayın.
  - Listeden doğrudan `Python 3.13`'ü seçtiğinizde editörünüz o kütüphaneleri görüp tüm kırmızı hataları silecektir.

## 6. Veri Görselleştirme (Grafiklerin Çizdirilmesi)
**Problem/Talep:** Ortam sorunlarının aşılmasının ardından kullanıcı, üretilen `data.csv` dosyasındaki Süt Miktarı ve Sıcaklık verilerini görsele döküp analiz edecek ikinci bir kod (`sutverimi_visualize.py`) yazılmasını talep etti.
**Çözüm:** `matplotlib.pyplot` kullanılarak veriler analiz edildi ve anında klasörün içerisine üç adet PNG kaydedildi:
1. `scatter_plot.png` (Sıcaklık ve Süt Miktarı Dağılım İlişkisi)
2. `sicaklik_hist.png` (Sıcaklık Değerlerinin Normal Dağılım Eğrisi Histogramı)
3. `sut_miktari_hist.png` (Süt Miktarının Normal Dağılım Eğrisi Histogramı)

**Final Sonucu:** Başarılı bir şekilde hem veri setlerinin normal dağılımı sağlandı, hem editör/çevre (environment) yönetiminin çözümü pratikleştirildi, hem de çıktılar analitik olarak grafiklere döküldü. İşlem başarıyla sonuçlandı.
