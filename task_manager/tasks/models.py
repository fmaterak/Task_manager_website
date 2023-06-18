from django.db import models

class Task(models.Model):
    # Define your fields here
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed
    
    def __str__(self):
        return self.title
