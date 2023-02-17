from django.db import models

class store(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=30)
    owner_email = models.CharField(max_length=30)
    license_number = models.CharField(max_length=20)
    mobile_number = models.IntegerField(default=0)

    def __str__(self):
        return self.store