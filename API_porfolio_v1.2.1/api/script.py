from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.http import HttpRequest
from .models import Programer
import os
from django.contrib import admin


@receiver(pre_delete, sender= Programer)
def delete_img(sender, instance, **kwargs):
    if os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

@admin.register(Programer)
class ProgramerAmin(admin.ModelAdmin):
    def delete_model(self, request: HttpRequest, obj: any) -> None:
        for i in obj:
            if os.path.isfile(i.image.path):
                os.remove(i.image.path)
        return super().delete_model(request, obj)

