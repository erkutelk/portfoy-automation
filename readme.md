# Django Muhasebe Yönetim Sistemi

Bu proje, işletmelerin gelir-gider yönetimini kolaylaştırmak için geliştirilmiş bir **Muhasebe Yönetim Sistemi**dir. 
Sistem, kullanıcı dostu arayüzü ve SQLite veritabanı ile finansal işlemleri takip etmeyi kolaylaştırır.

## 🚀 Özellikler

- **Ana Sayfa**
  - 📈 Toplam Aylık Gelir
  - 💰 Bekleyen & Ödenmesi Gereken Faturalar
  - 👥 En Son Eklenen Müşteriler
  - 📊 Aylık Gider Grafiği

- **Fatura Yönetimi**
  - ⏳ Son ödeme tarihi 3 günden az kalan faturaların listelenmesi
  - 💳 Ödenmesi gereken toplam tutarların gösterilmesi

- **Müşteri Yönetimi**
  - 📂 Müşteri bilgilerini ekleme, düzenleme ve listeleme

- **Raporlama Sayfası**
  - 📊 Aylık gelirleri aylara göre filtreleme
  - 💼 Aylık kâr hesaplama ve analiz

- **Ayarlar Sayfası**
  - ⚙️ Kullanıcı yönetimi ve sistem yapılandırmaları

## 🛠 Kullanılan Teknolojiler

- **Backend:** Django (Python)
- **Veritabanı:** SQLite
- **Frontend:** Django Template Engine (HTML, CSS, Bootstrap)

## 📥 Kurulum

Projeyi kendi bilgisayarınıza kurmak için aşağıdaki adımları izleyin:

### Depoyu Klonlayın

```sh
git clone https://github.com/kullanici_adiniz/muhasebe-yonetim-sistemi.git
cd muhasebe-yonetim-sistemi
```


### Veritabanını Oluşturun ve Migrasyonları Uygulayın

```sh
python manage.py migrate
```

### Yönetici Hesabı Oluşturun

```sh
python manage.py createsuperuser
```

### Uygulamayı Çalıştırın

```sh
python manage.py runserver
```

Tarayıcınızda **http://127.0.0.1:8000/** adresine giderek uygulamayı kullanabilirsiniz.