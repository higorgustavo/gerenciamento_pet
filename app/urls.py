from django.urls import path
from .views import cliente_views, pet_views, consulta_views, funcionario_views, autenticacao_views


urlpatterns = [
    path('listar-clientes', cliente_views.listar_clientes, name='listar-clientes'),
    path('cadastrar-clientes', cliente_views.cadastar_cliente, name='cadastrar-clientes'),
    path('detalhar-cliente/<int:id>', cliente_views.detalhar_cliente, name='detalhar-cliente'),
    path('editar-cliente/<int:id>', cliente_views.editar_cliente, name='editar-cliente'),
    path('remover-cliente/<int:id>', cliente_views.remover_cliente, name='remover-cliente'),
    path('cliente/<int:id>/cadastrar-pets', pet_views.cadastrar_pet, name='cadastrar-pets'),
    path('detalhar-pet/<int:id>', pet_views.detalhar_pet, name='detalhar-pet'),
    path('pet/<int:id>/cadastrar-consultas', consulta_views.cadastrar_consulta, name='cadastrar-consulta'),
    path('detalhar-consulta/<int:id>', consulta_views.detalhar_consulta, name='detalhar-consulta'),
    path('listar-funcionarios', funcionario_views.listar_funcionarios, name='listar-funcionarios'),
    path('cadastrar-funcionarios', funcionario_views.cadastrar_funcionario, name='cadastrar-funcionarios'),
    path('login', autenticacao_views.login_usuario, name='login'),
    path('logout', autenticacao_views.logout_usuario, name='logout'),
    path('enviar-consulta/<int:id>', consulta_views.enviar_email_consulta, name='enviar-consulta')
]

