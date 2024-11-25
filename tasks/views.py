from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa, Usuario
from .serializers import TarefaSerializer, UsuarioSerializer

class TarefaList(APIView):
    def get(self, request):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        usuario_id = request.data.get('usuario')
        if not usuario_id:
            return Response({"detail": "Usuário é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        tarefa_data = {
            'descricao': request.data.get('descricao'),
            'nome_setor': request.data.get('nome_setor'),
            'prioridade': request.data.get('prioridade'),
            'status': request.data.get('status'),
            'usuario': usuario.id  # Usando o ID do usuário
        }

        serializer = TarefaSerializer(data=tarefa_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Aqui vamos retornar os erros específicos do serializer
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TarefaDetail(APIView):
    def get(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        except Tarefa.DoesNotExist:
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Atualizando os campos conforme os dados da requisição
        tarefa.descricao = request.data.get('descricao', tarefa.descricao)
        tarefa.nome_setor = request.data.get('nome_setor', tarefa.nome_setor)
        tarefa.prioridade = request.data.get('prioridade', tarefa.prioridade)
        tarefa.status = request.data.get('status', tarefa.status)

        # Salvando a tarefa atualizada
        tarefa.save()

        # Retornando a tarefa atualizada
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        tarefa.delete()
        return Response({"detail": "Tarefa excluída com sucesso."}, status=status.HTTP_204_NO_CONTENT)
    

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

class CadastroUsuario(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
