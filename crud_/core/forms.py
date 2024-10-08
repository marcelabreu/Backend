from django import forms
from .models import Cliente, Produto, Pedido, Assinatura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produtos']
        widgets = {
            'produtos': forms.CheckboxSelectMultiple,
        }
class AssinaturaForm(forms.ModelForm):
    class Meta:
        model = Assinatura
        fields = ['cliente', 'data_inicio', 'data_fim', 'ativo']