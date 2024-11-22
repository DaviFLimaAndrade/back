from django.urls import path
from .views import TarefaList, TarefaDetail, UsuarioList, CadastroUsuario

urlpatterns = [
    path('tarefas/', TarefaList.as_view(), name='lista_tarefas'),
    path('tarefas/<int:pk>/', TarefaDetail.as_view(), name='detalhe_tarefa'),
    path('cadastrar_usuario/', CadastroUsuario.as_view(), name='cadastrar_usuario'),
    path('usuarios/', UsuarioList.as_view(), name='listar_usuarios'),
]
