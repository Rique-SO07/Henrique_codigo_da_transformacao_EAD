from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto

# 1. LISTAR PRODUTOS (Com Busca e Paginação)
def listar_produtos(request):
    termo_busca = request.GET.get('busca', '')
    
    if termo_busca:
        produtos_lista = Produto.objects.filter(nome__icontains=termo_busca)
    else:
        produtos_lista = Produto.objects.all()

    # Exibir no máximo 3 produtos por página
    paginator = Paginator(produtos_lista, 3) 
    numero_da_pagina = request.GET.get('page')
    produtos_paginados = paginator.get_page(numero_da_pagina)

    return render(request, 'produtos/listar.html', {
        'produtos': produtos_paginados, 
        'termo_busca': termo_busca
    })

# 2. CADASTRAR PRODUTO (A função que estava faltando!)
def cadastrar_produto(request):
    if request.method == "POST":
        Produto.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            quantidade=request.POST.get('quantidade')
        )
    return redirect('listar_produtos')

# 3. ATUALIZAR PRODUTO
def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/editar.html', {'produto': produto})

# 4. EXCLUIR PRODUTO
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')