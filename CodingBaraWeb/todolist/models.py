from django.db import models

# Create your models here.
class ToDoList(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")