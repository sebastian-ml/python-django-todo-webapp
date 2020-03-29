from django.utils import timezone
from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    when_finished = models.TimeField(default=timezone.now)

    def __str__(self):
        return f'{self.pk} {self.text}'
