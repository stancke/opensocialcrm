from django.db import models

class Note(models.Model):
    note = models.CharField("Note", max_length=100)

from tests.customapp import listeners
listeners.start_listening()