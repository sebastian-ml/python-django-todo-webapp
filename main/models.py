from django.db import models


class Task(models.Model):
    """Contain details about each task."""
    text = models.CharField(max_length=30)
    finished = models.BooleanField(default=False)
    when_finished_h = models.TimeField(null=True, default=None)
    when_finished_date = models.DateField(null=True, default=None)

    def __str__(self):
        return f'{self.pk} {self.text}'
