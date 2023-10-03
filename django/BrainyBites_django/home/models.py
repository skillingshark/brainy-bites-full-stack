from django.db import models
from django.contrib.auth.models import AbstractUser #For Signup 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150 ,unique=True)
#     password = models.CharField(max_length=128)
    
    
    # To change contact object into name of the sender 
    # we are writing a function
    def __str__(self):
        return self.name
        # return " Name: " + self.name + " Email: " +  self.email
    
    # def __str__(self):
    #     return self.username

#Check djangoproject.com documentation for more help 

# after making changes into models.py use python manage.py makemigrations

# makemigration - create changes and store in a file 
# migrate - apply the pending changes created by make migrations