from django.db import models
from django.utils import timezone

# Create your models here.
class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ("ALL", "FULLSTACK"),
        ("UI", "FRONTEND"),
        ("DATA", "BACKEND"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/')
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=5, choices=APP_TYPE_CHOICE)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    