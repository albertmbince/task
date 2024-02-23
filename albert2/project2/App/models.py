from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    dname=models.CharField(max_length=50)
    birthdate=models.DateField( auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=50)
    teacher=models.CharField( max_length=50)
    address=models.CharField( max_length=150)
    city=models.CharField(max_length=50)
    subjects=models.CharField( max_length=250)
    state=models.CharField( max_length=50)
    country=models.CharField( max_length=50)
    image=models.ImageField( upload_to='gallery')
    phonenumber=models.PositiveIntegerField()
    email=models.EmailField( max_length=254)
    zipcode=models.PositiveIntegerField()
    def __str__(self):
        return self.name
