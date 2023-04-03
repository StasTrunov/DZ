from django.db import models

# Create your models here.




class FClub(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    # championship = models.ManyToManyField(Championship)

    def __str__(self):
        return self.name

class Championship(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=60)
    club = models.ForeignKey(FClub, models.CASCADE)

    def __str__(self):
        return self.name


    
class FPlayer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    height = models.FloatField()
    costs = models.FloatField()
    club = models.ManyToManyField(FClub)

    def __str__(self):
        return self.name
