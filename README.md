# Python ile XOX Oyunu (Bilgisayara Karşı) 

Bu proje, Python programlama dilinin temel yapı taşlarını ve matris mantığını kavramak amacıyla geliştirilmiş, terminal tabanlı bir **XOX (Tic-Tac-Toe)** oyunudur. Oyuncu (X), karşı hamleler yapan bir bilgisayar algoritmasına (O) karşı mücadele eder.

## Özellikler
* **PvE Modu:** Bilgisayara karşı oynanır.
* **Akıllı Hamle Kontrolü:** Bilgisayar, hamle yapmadan önce tahtayı analiz eder:

Hücum: Eğer bir sonraki hamlede kazanabiliyorsa o hamleyi yapar.

Savunma: Eğer oyuncu bir sonraki hamlede kazanacaksa o kareyi kapatarak oyuncuyu engeller.

Öncelik Sistemi: Merkez kareyi ve köşeleri tutmaya odaklanarak stratejik bir avantaj sağlar.
* **Hata Yönetimi:** Kullanıcının geçersiz veri girişlerine (harf, sınır dışı sayı vb.) karşı `try-except` blokları ile koruma.
* **Dinamik Tahta:** Her hamleden sonra güncellenen görsel terminal arayüzü.

## Teknik Detaylar
* **Veri Yapıları:** Oyun tahtası için iç içe listeler (2D Matrix) kullanıldı.
* **Algoritma:** Bilgisayarın hamleleri için çok aşamalı bir kontrol fonksiyonu tasarlandı.
* **Döngüler & Koşullar:** Oyunun sürekliliği için `while` döngüsü; kazanma durumları için ise kapsamlı `if-elif-else` kontrol blokları kullanıldı.

## Nasıl Çalıştırılır?
Projeyi bilgisayarınıza indirin (Klonlayın):
```bash
git clone https://github.com/faruksrcn21-ux/xox-oyunu.git
cd xox-oyunu
```
