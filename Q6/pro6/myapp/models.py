from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title


class Attendee(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='attendees'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name