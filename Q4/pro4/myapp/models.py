from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    summary = models.TextField()

    def __str__(self):
        return self.title