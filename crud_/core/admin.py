from django.contrib import admin
from .models import Cliente, Produto, Pedido, PedidoProduto, Assinatura

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(PedidoProduto)
admin.site.register(Assinatura)