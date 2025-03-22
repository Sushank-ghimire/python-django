from django.db import models
from django.utils import timezone

# Create your models here.
class Todos(models.Model):
    WORK_VALUE = [
        ("Important", "Have to done quickly."),
        ("Less Important", "Can be done after some time."),
        ("No Hurry", "Can be done after more time just chill.")
    ]
    
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    date_added = models.DateField(default=timezone.now)
    importance = models.CharField(choices=WORK_VALUE, max_length=20)
    done_upto = models.DateField(timezone.now())

    def __str__(self):
        return self.title
    
    