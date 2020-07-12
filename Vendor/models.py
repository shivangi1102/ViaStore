from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Regisvendor(models.Model):
    ven_id=models.AutoField(primary_key=True)
    mobileno = models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    gstno = models.CharField(max_length=10)
    adhar = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ven_id)





class ProductDetails(models.Model):
    id=models.AutoField(primary_key=True)
    prod_tittle= models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    price=models.CharField(max_length=5)
    stock=models.CharField(max_length=3)
    imag=models.ImageField(upload_to='Vendor/images', default="")
    ven_id=models.ForeignKey(Regisvendor,on_delete=models.CASCADE)


    def __str__(self):
        return self.prod_tittle