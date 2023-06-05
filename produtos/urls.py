from django.urls import path
from produtos.views import index, listagem

urlpatterns = [
    path('', index, name='index'),
    path('listagem/', listagem, name='listagem'),
]