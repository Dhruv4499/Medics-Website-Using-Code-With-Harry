from django.db import models
      
class Blog_Category(models.Model):
    id = models.AutoField(primary_key=True)  
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type  
