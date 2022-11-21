from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField( 
        max_length=100,
        blank= False,
        null= False,

    )

    password = models.CharField(
        max_length= 100,
        null= False,
        blank= False
    )

    email = models.EmailField(
        unique= True,
        blank= False,
        null= False,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['password','username' ]

    def __str__(self):
        return self.username
    