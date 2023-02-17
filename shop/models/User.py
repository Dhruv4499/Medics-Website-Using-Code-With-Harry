from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    mobile_number = models.IntegerField(default=0)
    email = models.EmailField(max_length=25)
    address = models.CharField(max_length=60)
    security_question = models.CharField(max_length=30)
    security_answer = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname + '' + lastname