from django.db import models
CHOICES = [
    ("sim", 'sim'),
    ("nao", 'não'),
]
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=False, blank=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    disponivel = models.CharField(max_length=100, choices=CHOICES)
    
def __str__(self):
    return self.nome