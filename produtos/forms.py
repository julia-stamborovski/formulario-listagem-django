from django import forms
from .models import Produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['',]
        labels = {
            'nome' : 'Nome do Produto',
            'descricao': 'Descrição do Produto',
            'preco' : 'Valor do Produto',
            'disponivel': 'Disponível para venda'
        }
  
    widgets = {
      'nome': forms.TextInput(),
      'descricao': forms.Textarea(),
      'preco': forms.DecimalField(),
      'disponivel': forms.Select(),
    }

   