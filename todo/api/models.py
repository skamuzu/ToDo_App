from django.db import models

# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=600, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    task_completed = models.BooleanField(default=False)
    image = models.ImageField(default = "default.jpg")
    
    def __str__(self):
        return f"{self.task}, Completed: {self.task_completed}"