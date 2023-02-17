from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images',default='')
    quantity = models.IntegerField(default=1)
    catagory = models.CharField(max_length=30,default=0)

    def __str__(self):
        return self.name