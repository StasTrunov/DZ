from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=250)
    coast = models.FloatField()
    version = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Mail(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.login


class Account(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    coast = models.FloatField(default=0, )
    description = models.TextField(null=True, blank=True)
    game = models.ManyToManyField(Game)
    mail = models.ForeignKey(Mail, models.CASCADE)
