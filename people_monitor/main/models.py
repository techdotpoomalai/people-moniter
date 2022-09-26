from django.db import models

# Create your models here.

# class Register (models.Model):
#     register_id=models.AutoField((""),primary_key=True)
#     country=models.CharField((""), max_length=30)
#     state=models.CharField((""), max_length=30)
#     email=models.EmailField((""), max_length=254)
#     phone=models.CharField((""), max_length=15)
#     frist_name=models.CharField((""), max_length=30)
#     last_name=models.CharField((""), max_length=30)

class Create_user(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.CharField(max_length=50)