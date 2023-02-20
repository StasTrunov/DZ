from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateField(blank=True, null=True)
    like = models.PositiveIntegerField(default = 0)
    dislike = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.name}"
    
    def __gt__(self, other):
        return self.like > other.like
    
    
class Tennis_players(models.Model):
    name = models.CharField(max_length=20)
    age = models.FloatField()
    height = models.FloatField()
    ranked_in_ATP = models.FloatField()
    majors = models.PositiveIntegerField(default = 0)
    like = models.PositiveIntegerField(default = 0)
    dislike = models.PositiveIntegerField(default = 0)


    def __str__(self):
        return f"{self.name}"


class Prog_languages(models.Model):
    name = models.CharField(max_length=20)
    date_of_creation = models.DateField(blank=True, null=True)
    like = models.PositiveIntegerField(default = 0)
    dislike = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.name}"

