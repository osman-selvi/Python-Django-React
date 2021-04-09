# DJReact

Django is a Python framework.

## General Information
### What is Django?
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.
### Where did Django Come From?
Django was initially developed between 2003 and 2005 by a web team who were responsible for creating and maintaining newspaper websites.
### 5 Best Python Frameworks
- Django
- Flask
- Web2Py
- Pyramid
- Bottle
### What does Django code look like?
When a request is received the application works out what is needed based on the URL and possibly information in POST data or GET data.
### What is MTV?
###### Models: Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database. 

##### Templates: A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. 

###### View: A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates

- After creating the project file, you need to activate your env structure. For active env,

```bash
   source env/bin/activate
```

## Installation

Use the package manager [django](https://docs.djangoproject.com/en/3.1/topics/install/) to install django.

```bash
 pip install django
```

Use the package rest_framework [rest_framework](https://www.django-rest-framework.org/) to install django.

```bash
 pip install djangorestframework
```

create django start project

```bash
 django-admin startproject djreact
```

got to src directory 

```bash
 django-admin startproject djreact
```

## Usage

Run the Django project
```bash
 python manage.py runserver
```

Create Superuser  
```python
python manage.py createsuperuser
```

For the applications you define, 
```python
python manage.py startapp article
```
To adjust the django setting, you can use settings.py. Checked rest_framework [rest_framework](https://www.django-rest-framework.org/)

## Note
For detailed information, please check the project in detail.

## License
[MIT](https://osmanselvi.com)