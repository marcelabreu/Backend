from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # URLs para Cliente
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('clientes/update/<int:id>/', views.cliente_update, name='cliente_update'),
    path('clientes/delete/<int:id>/', views.cliente_delete, name='cliente_delete'),

    # URLs para Produto
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/create/', views.produto_create, name='produto_create'),
    path('produtos/update/<int:id>/', views.produto_update, name='produto_update'),
    path('produtos/delete/<int:id>/', views.produto_delete, name='produto_delete'),

    # URLs para Pedido
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedidos/create/', views.pedido_create, name='pedido_create'),
    path('pedidos/update/<int:id>/', views.pedido_update, name='pedido_update'),
    path('pedidos/delete/<int:id>/', views.pedido_delete, name='pedido_delete'),

    # URLs para Assinatura
    path('assinaturas/', views.assinatura_list, name='assinatura_list'),
    path('assinaturas/create/', views.assinatura_create, name='assinatura_create'),
    path('assinaturas/update/<int:id>/', views.assinatura_update, name='assinatura_update'),
    path('assinaturas/delete/<int:id>/', views.assinatura_delete, name='assinatura_delete'),
]
