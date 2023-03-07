from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=250)
    costs = models.FloatField()
    verion = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mail(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class Account(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    costs = models.FloatField()
    description = models.TextField(null=True,blank=True)
    game = models.ManyToManyField(Game)
    mail = models.ForeignKey(Mail, models.CASCADE)


    


    

