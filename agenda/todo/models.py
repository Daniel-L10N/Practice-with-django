from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length =100, blank= False, null= False)
    date = models.DateField(default = date.today)
    estimate_end = models.DateField( blank=False, null=False)
    priority = models.IntegerField(default=3)
    description = models.TextField()

    def __str__(self):
        return self.title