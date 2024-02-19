from django.db import models
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Programer(models.Model):
    fullname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 50)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/programers', null=True)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Programer, self).delete(*args, **kwargs)

    def __str__(self):
        return self.nickname