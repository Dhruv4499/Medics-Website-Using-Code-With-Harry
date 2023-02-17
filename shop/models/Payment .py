from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    amount = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.id
