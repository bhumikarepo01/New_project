from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number = models.CharField(max_length=15)
    # courses =models.ManyToManyField(Course)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name
