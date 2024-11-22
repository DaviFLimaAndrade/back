from rest_framework import serializers
from .models import Tarefa, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email']

class TarefaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())  # Alterado para o ID do usuário, não o objeto completo.

    class Meta:
        model = Tarefa
        fields = ['id', 'descricao', 'nome_setor', 'prioridade', 'status', 'data_cadastro', 'vinculado', 'usuario']
