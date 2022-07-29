from django.db import models

# Create your models here.


class ProductDetails(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=100)
