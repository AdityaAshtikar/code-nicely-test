from django.db import models
from django.conf import settings
from django.utils import timezone


class Note(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Shared(models.Model):
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_level = models.BooleanField(
        default=0, help_text="Default Access is read-only")
    created_date = models.DateTimeField(
        default=timezone.now)
