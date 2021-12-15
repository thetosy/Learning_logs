from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """topic the user is currently learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """returns the model in a string format"""
        return self.text


class Entry(models.Model):
    """entries based on what was learnt about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        """extra information on how to handle the model"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """display the model in a string format"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text


