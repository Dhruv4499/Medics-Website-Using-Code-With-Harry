from django.db import models
        
class Role(models.Model):
    id = models.AutoField(primary_key=True,default='')  
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type
 