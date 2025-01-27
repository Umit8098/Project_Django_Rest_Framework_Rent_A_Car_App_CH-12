<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Rent_A_Car_App</h1>

<p align="center">🚗 Müşterilerin araç kiralamasını ve yöneticilerin araç envanterini yönetmesini sağlayan bir API uygulaması 🚗</p>


<!-- <div align="center">
  <h3>
    <a href="http://umit8104.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="http://umit8104.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Endpoints](#api-endpoints)
  - [User/Authentication Endpoints:](#userauthentication-endpoints)
  - [API/CAR Endpoints:](#apicar-endpoints)
- [API Testing](#api-testing)
- [Overview](#overview)
  - [Kullanıcı Doğrulama Testi](#kullanıcı-doğrulama-testi)
  - [Rent\_A\_Car\_App CRUD Testi](#rent_a_car_app-crud-testi)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [Örnek Kullanım](#örnek-kullanım)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)


## API Endpoints

Bu API aşağıdaki endpoint'leri sağlar:

### User/Authentication Endpoints:

| Method | URL                                                          | Açıklama            |
|--------|--------------------------------------------------------------|---------------------|
| POST   | `https://umit8104.pythonanywhere.com/users/register/`        | Yeni kullanıcı kaydı|
| POST   | `https://umit8104.pythonanywhere.com/users/auth/login/`      | Kullanıcı girişi    |
| POST   | `https://umit8104.pythonanywhere.com/users/auth/logout/`     | Kullanıcı çıkışı    |


### API/CAR Endpoints:

| Method | URL                                                     | Açıklama                         |
|--------|---------------------------------------------------------|----------------------------------|
| GET    | `https://umit8104.pythonanywhere.com/api/car/`          | Tüm araçları listele             |
| POST   | `https://umit8104.pythonanywhere.com/api/reservation/`  | Yeni rezervasyon oluştur         |
| GET    | `https://umit8104.pythonanywhere.com/api/reservation/1` | Belirli bir rezervasyon detayları|
| PUT    | `https://umit8104.pythonanywhere.com/api/reservation/1` | Rezervasyonu güncelle            |
| DELETE | `https://umit8104.pythonanywhere.com/api/reservation/1` | Rezervasyonu sil                 |


## API Testing

Postman Collection, API'nizin her bir endpoint'ini test etmek için gerekli istekleri içerir. API'nin işlevselliğini hızlı bir şekilde anlamak için kullanabilirsiniz.

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-7e6a0325-086d-4ed1-bd4d-d46131a26b88?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Blog App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-7e6a0325-086d-4ed1-bd4d-d46131a26b88?action=share&creator=17531143)


## Overview

Rent A Car API uygulaması, araç kiralama süreçlerini kolaylaştırmayı hedefleyen bir sistemdir. Uygulamanın özellikleri:
- Müşteriler:
  - Belirli tarih aralıklarında uygun araçları listeleyebilir ve rezerve edebilir.
  - Rezervasyonlarını görüntüleyebilir veya iptal edebilir.
  - Aynı tarih aralığında birden fazla araç kiralayamaz.
- Yöneticiler:
  - Araç, müşteri ve rezervasyon tabloları için CRUD işlemleri yapabilir.
- Geçmiş tarihler listelenmez ve rezerve edilen araçlar tekrar rezerve edilemez.

### Kullanıcı Doğrulama Testi
<!-- ![screenshot](project_screenshot/Rent_A_Car_User_Auth_Test_Postman.gif) -->
<img src="project_screenshot/Rent_A_Car_User_Auth_Test_Postman.gif" alt="Kullanıcı Doğrulama Testi" width="400"/>
➡ *Postman ile kullanıcı doğrulama işlemleri için yapılan test sürecini görebilirsiniz.*

---

### Rent_A_Car_App CRUD Testi
<!-- ![screenshot](project_screenshot/Rent_A_Car_App_Test_Postman.gif) -->
<img src="project_screenshot/Rent_A_Car_App_Test_Postman.gif" alt="Rent_A_Car_App CRUD Testi" width="400"/>
➡ *Araç kiralama API'si üzerindeki CRUD işlemlerini Postman ile test etme.*


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->
Bu proje aşağıdaki araçlar ve kütüphanelerle inşa edilmiştir:
- [Django Rest Framework](https://www.django-rest-framework.org/) - REST API geliştirmek için kullanılan güçlü bir framework.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Kullanıcı doğrulama ve yetkilendirme modülü.
- [django-filter](https://django-filter.readthedocs.io/en/stable/): Gelişmiş filtreleme özellikleri için kullanılan bir kütüphane.


## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Rent_A_Car_App_CH-12) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Rent_A_Car_App_CH-12.git

# Install dependencies
    $ python -m venv env
    $ python -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...
"""

# Run the app
    $ python manage.py runserver
```

- Uygulamayı klonladıktan ve bağımlılıkları yükledikten sonra şu adımları izleyebilirsiniz:

### Örnek Kullanım

1. **Login Request:**
   - URL: `https://umit8104.pythonanywhere.com/users/auth/login/`
   - Method: `POST`
   - Body (JSON):
```json
  {
    "email": "mary@gmail.com",
    "password": "mary123456"
  }
```

1. **Kiralama Oluşturma:**
   - URL: `https://umit8104.pythonanywhere.com/api/reservation/`
   - Method: `POST`
   - Headers:
  
```text
  Authorization: Token <login olunduğunda dönen token key>
```
- 
  - Body (JSON):

```json
  {
    "customer": 1,
    "car": 2,
    "start_date": "2025-05-26",
    "end_date": "2025-05-28"
}
```

## About This Project

- It is an API application developed to digitize and optimize car rental processes. It offers special capabilities to both customers and managers:
- Customers:
  - Can specify a date range and list available vehicles. Past dates are not listed.
  - A vehicle can be reserved within the selected date range, but a second vehicle cannot be rented within the same date range.
  - A reserved vehicle cannot be reserved on those dates.
  - Can list reservations.
  - Can delete reservations.
- Managers:
  - Car table CRUD operations
  - Customer (User) table CRUD operations
  - Reservation table CRUD operations

<hr>

- Araç kiralama süreçlerini dijitalleştirmek ve optimize etmek amacıyla geliştirilmiş bir API uygulamasıdır. Hem müşterilere hem de yöneticilere özel yetenekler sunar:
- Müşteriler:
  - Tarih aralığı belirtip müsait araç listeleyebilir. Geçmiş tarihler listelenmez.
  - Seçilen tarih aralığında araç rezerve edilebilir, ancak aynı tarih aralığında ikinci bir araç kiralayamaz.
  - Rezerve edilmiş bir aracı, o tarihlerde rezerve edemez.
  - Rezervasyonlarını listeyebilir.
  - Rezervasyonlarını silebilir.
- Yöneticiler:
  - Araba tablosu CRUD işlemleri
  - Müşteri (Kullanıcı) tablosu CRUD işlemleri
  - Reservasyon tablosu CRUD işlemleri


## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/) - REST API oluşturmak için kullanılan framework.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Kullanıcı doğrulama için kullanıldı.
- [django-filter](https://django-filter.readthedocs.io/en/stable/): Gelişmiş filtreleme özellikleri için kullanıldı.


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- **GitHub** [@Umit8098](https://github.com/Umit8098)

- **LinkedIn** [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
