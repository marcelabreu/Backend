from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Produto, Pedido, Assinatura
from .forms import ClienteForm, ProdutoForm, PedidoForm, AssinaturaForm

def home(request):
    return render(request, 'core/home.html')

#View Client

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'core/cliente_form.html', {'form': form})

def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'core/cliente_form.html', {'form': form})

def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'core/cliente_confirm_delete.html', {'cliente': cliente})

# Views para Produto
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'core/produto_list.html', {'produtos': produtos})

def produto_create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'core/produto_form.html', {'form': form})

def produto_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'core/produto_form.html', {'form': form})

def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'core/produto_confirm_delete.html', {'produto': produto})

# Views para Pedido
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/pedido_list.html', {'pedidos': pedidos})

def pedido_create(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        pedido = form.save(commit=False)
        pedido.save()
        form.save_m2m()
        return redirect('pedido_list')
    return render(request, 'core/pedido_form.html', {'form': form})

def pedido_update(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        pedido = form.save(commit=False)
        pedido.save()
        form.save_m2m()
        return redirect('pedido_list')
    return render(request, 'core/pedido_form.html', {'form': form})

def pedido_delete(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido_list')
    return render(request, 'core/pedido_confirm_delete.html', {'pedido': pedido})

# Views para Assinatura
def assinatura_list(request):
    assinaturas = Assinatura.objects.all()
    return render(request, 'core/assinatura_list.html', {'assinaturas': assinaturas})

def assinatura_create(request):
    form = AssinaturaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('assinatura_list')
    return render(request, 'core/assinatura_form.html', {'form': form})

def assinatura_update(request, id):
    assinatura = get_object_or_404(Assinatura, id=id)
    form = AssinaturaForm(request.POST or None, instance=assinatura)
    if form.is_valid():
        form.save()
        return redirect('assinatura_list')
    return render(request, 'core/assinatura_form.html', {'form': form})

def assinatura_delete(request, id):
    assinatura = get_object_or_404(Assinatura, id=id)
    if request.method == 'POST':
        assinatura.delete()
        return redirect('assinatura_list')
    return render(request, 'core/assinatura_confirm_delete.html', {'assinatura': assinatura})