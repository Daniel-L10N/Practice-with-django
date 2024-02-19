from django.contrib import admin
from .models import Programer 
from django.http import HttpRequest
import os

admin.site.register(Programer)

# @admin.register(Programer)
# class ProgramerAmin(admin.ModelAdmin):
#     def delete_model(self, request: HttpRequest, obj: any) -> None:
#         for i in obj:
#             if os.path.isfile(i.image.path):
#                 os.remove(i.image.path)
#         return super().delete_model(request, obj)