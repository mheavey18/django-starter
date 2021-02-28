# django-starter

A basic Django app including auth functionality
It uses a custom user model inheriting from AbstractUser which can be extended
in project/app/models.py

It has basic template for sign up, log in, and view users
in project/templates/

initialized with `django-admin startproject project`
then `python manage.py startapp app`

initialize the mysql db with
`python manage.py migrate`

start up a server on your local machine with
`python manage.py runserver`
then go to
http://localhost:8000

use the Django database API with
`python manage.py shell`
