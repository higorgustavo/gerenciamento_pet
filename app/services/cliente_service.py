from ..models import Cliente


def listar_clientes():
    return Cliente.objects.all()


def get_cliente(id):
    return Cliente.objects.get(id=id)


def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, cpf=cliente.cpf, email=cliente.email,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao,
                           endereco=cliente.endereco)


def editar_cliente(cliente_antigo, cliente_novo):
    cliente_antigo.nome = cliente_novo.nome
    cliente_antigo.cpf = cliente_novo.cpf
    cliente_antigo.email = cliente_novo.email
    cliente_antigo.data_nascimento = cliente_novo.data_nascimento
    cliente_antigo.profissao = cliente_novo.profissao
    cliente_antigo.endereco = cliente_novo.endereco
    cliente_antigo.save(force_update=True)


def remover_cliente(cliente):
    cliente.delete()
