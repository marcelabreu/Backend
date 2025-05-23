# Generated by Django 5.1.1 on 2024-10-08 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(through='core.PedidoProduto', to='core.produto'),
        ),
    ]
