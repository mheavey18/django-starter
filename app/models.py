from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    this is the user model which can be updated
    it inherits form AbstractUser to get the base auth functionality available from Django
    documentation here: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
    '''
    pass

# add other base models for your app here
