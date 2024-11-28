from django.shortcuts import render

from rest_framework import generics
from .models import Receita
from .serializers import ReceitaSerializer

class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()  # Retorna todas as receitas
    serializer_class = ReceitaSerializer
