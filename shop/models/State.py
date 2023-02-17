from django.db import models

class State(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name