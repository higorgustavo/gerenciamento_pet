from ..models import Pet


def listar_pets_cliente(id):
    pets = Pet.objects.filter(dono_id=id).all()
    return pets


def get_pet(id):
    pet = Pet.objects.get(id=id)
    return pet


def cadastrar_pet(pet):
    pet_bd = Pet.objects.create(nome=pet.nome, nascimento=pet.nascimento, categoria=pet.categoria,
                                cor=pet.cor, dono=pet.dono)
    pet_bd.save()


def editar_pet(pet_antigo, pet_novo):
    pet_antigo.dono = pet_novo.dono
    pet_antigo.nome = pet_novo.nome
    pet_antigo.nascimento = pet_novo.nascimento
    pet_antigo.categoria = pet_novo.categoria
    pet_antigo.cor = pet_novo.cor
    pet_antigo.save(force_update=True)
