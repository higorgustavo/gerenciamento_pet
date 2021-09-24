from ..models import Consulta


def listar_consultas_pet(id):
    consultas = Consulta.objects.filter(pet_id=id).all().order_by('-data')
    return consultas


def listar_consultas_cliente(id):
    consultas = Consulta.objects.filter(pet__dono_id=id).all().order_by('-data')
    return consultas


def get_consulta(id):
    consulta = Consulta.objects.get(id=id)
    return consulta


def cadastrar_consulta(consulta):
    consulta_db = Consulta.objects.create(pet=consulta.pet, motivo_consulta=consulta.motivo_consulta,
                                          peso_atual=consulta.peso_atual,
                                          medicamento_atual=consulta.medicamento_atual,
                                          medicamentos_prescritos=consulta.medicamentos_prescritos,
                                          exames_prescritos=consulta.exames_prescritos)
