from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

def index(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('listagem')
        else:
            messages.error(request, 'Erro ao cadastrar o produto. Verifique os campos.')
            return redirect('index')  
    else:
        form = ProdutoForm()

    return render(request, 'produtos/index.html', {'form': form})

def listagem(request):
    produtos = Produto.objects.order_by('preco')
    return render(request, 'produtos/listagem.html', {'produtos': produtos})
