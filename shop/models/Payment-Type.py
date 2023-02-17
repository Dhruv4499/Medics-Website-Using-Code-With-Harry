from django.db import models

class Payment_Type(models.Model):
    id = models.AutoField(primary_key=True,default=0)  
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type
   