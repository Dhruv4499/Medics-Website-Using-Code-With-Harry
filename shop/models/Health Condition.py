from django.db import models
   
class Health_Condition(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name      