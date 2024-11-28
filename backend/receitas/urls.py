from django.urls import path
from .views import ReceitaList

urlpatterns = [
    path('receitas/', ReceitaList.as_view(), name='receitas-list'),  # Endpoint /receitas/
]
