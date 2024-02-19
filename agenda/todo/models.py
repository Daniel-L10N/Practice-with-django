from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length =100, blank= False, null= False)
    description = models.TextField()
    date = models.DateField(default = date.today)
    estimate_end = models.DateField( blank=False, null=False)
    preority = models.IntegerField(default=3)

    def __str__(self):
        return self.title