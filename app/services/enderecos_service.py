from ..models import Endereco


def get_endereco(id):
    return Endereco.objects.get(id=id)


def cadastrar_endereco(endereco):
    return Endereco.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)


def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo


def remover_endereco(endereco):
    endereco.delete()
