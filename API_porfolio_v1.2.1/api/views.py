from rest_framework import viewsets
from .serializer import ProgramerSerializer
from .models import Programer

class ProgramerViewSet(viewsets.ModelViewSet):
    queryset = Programer.objects.all()
    serializer_class = ProgramerSerializer
    


