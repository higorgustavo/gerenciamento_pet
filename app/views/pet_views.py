from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms.pet_form import PetForm
from ..entidades import pet
from ..services import pet_service, cliente_service, consulta_service


@login_required()
def detalhar_pet(request, id):
    pet_selecionado = pet_service.get_pet(id)
    consultas = consulta_service.listar_consultas_pet(id)
    context = {
        "pet": pet_selecionado,
        "consultas": consultas
    }
    return render(request, 'pets/detalhar_pet.html', context)


@login_required()
def cadastrar_pet(request, id):
    if request.method == "POST":
        form_pet = PetForm(request.POST)
        dono = cliente_service.get_cliente(id)
        if form_pet.is_valid():
            nome = form_pet.cleaned_data["nome"]
            nascimento = form_pet.cleaned_data["nascimento"]
            categoria = form_pet.cleaned_data["categoria"]
            cor = form_pet.cleaned_data["cor"]
            pet_novo = pet.Pet(dono=dono, nome=nome, nascimento=nascimento, categoria=categoria,
                               cor=cor)
            pet_service.cadastrar_pet(pet_novo)
            return redirect('listar-clientes')
    else:
        form_pet = PetForm()

    context = {
        'form_pet': form_pet
    }
    return render(request, 'pets/form_pet.html', context)


@login_required()
def editar_pet(request, id):
    pet_antigo = pet_service.get_pet(id)
    form_pet = PetForm(request.POST or None, instance=pet_antigo)
    if form_pet.is_valid():
        dono = form_pet.cleaned_data["dono"]
        nome = form_pet.cleaned_data["nome"]
        cor = form_pet.cleaned_data["cor"]
        nascimento = form_pet.cleaned_data["nascimento"]
        categoria = form_pet.cleaned_data["categoria"]
        pet_novo = pet.Pet(dono=dono, nome=nome, cor=cor, nascimento=nascimento,
                           categoria=categoria)
        pet_service.editar_pet(pet_antigo, pet_novo)
        return redirect('listar_pets')

    context = {
        'form_pet': form_pet
    }
    return render(request, 'pets/form_pet.html', context)
