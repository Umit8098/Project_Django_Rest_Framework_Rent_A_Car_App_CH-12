<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Rent_A_Car_App</h1>


<div align="center">
  <h3>
    <a href="http://umit8104.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="http://umit8104.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview
- Rent_A_Car_App User/Auth Test On Postman
![screenshot](project_screenshot/Rent_A_Car_User_Auth_Test_Postman.gif)

---

![screenshot](project_screenshot/quiz_app_quiz.gif)

---

![screenshot](project_screenshot/quiz_app_user.gif)

---

![screenshot](project_screenshot/quiz_app_shema.jpg)


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework


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

## About This Project
- Rent A Car Application API service.
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

- Rent A Car Application API service.
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
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
