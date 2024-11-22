# Generated by Django 5.1.3 on 2024-11-21 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('nome_setor', models.CharField(max_length=100)),
                ('prioridade', models.CharField(choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')], max_length=10)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('a_fazer', 'A Fazer'), ('fazendo', 'Fazendo'), ('pronto', 'Pronto')], default='a_fazer', max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='tasks.usuario')),
            ],
        ),
    ]
