from django.db import models

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default='')
    MFD = models.DateField(default='')
    expire_date = models.DateField(default='')
    quantity = models.IntegerField(default='')

    def __str__(self):
        return self.name
  