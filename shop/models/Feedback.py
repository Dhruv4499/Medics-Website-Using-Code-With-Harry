from django.db import models

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)  
    description = models.TextField(max_length=250,blank=True)
    date = models.DateField()
    user.id = models.ForeignKey(user,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self._type
