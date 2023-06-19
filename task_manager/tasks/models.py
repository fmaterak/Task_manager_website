from django.db import models
import datetime

class Task(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    due_date = models.DateField(default=datetime.date.today) 
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
