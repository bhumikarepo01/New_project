
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name



class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title