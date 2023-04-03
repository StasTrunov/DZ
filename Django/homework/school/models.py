from django.db import models

# Create your models here.




class Student(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.FloatField()
    email = models.CharField(max_length=50)



    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=10)
    age = models.FloatField()
    students = models.ForeignKey(Student, models.CASCADE)



    def __str__(self):
        return self.name


    
class School(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    students = models.ForeignKey(Student, models.CASCADE)
    clases = models.ForeignKey(Class, models.CASCADE)


    def __str__(self):
        return self.name