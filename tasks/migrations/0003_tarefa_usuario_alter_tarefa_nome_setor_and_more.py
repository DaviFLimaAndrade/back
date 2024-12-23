# Generated by Django 5.1.3 on 2024-11-22 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_tarefa_usuario_tarefa_vinculado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='nome_setor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='vinculado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
