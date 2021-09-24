from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..entidades import cliente, endereco
from ..services import cliente_service, enderecos_service, pet_service, consulta_service
from ..forms.cliente_form import ClienteForm
from ..forms.endereco_form import EnderecoForm


@login_required()
def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    context = {
        "clientes": clientes
    }
    return render(request, "clientes/lista_clientes.html", context)


@login_required()
def detalhar_cliente(requet, id):
    cliente_selecionado = cliente_service.get_cliente(id)
    pets = pet_service.listar_pets_cliente(id)
    consultas = consulta_service.listar_consultas_cliente(id)
    context = {
        "cliente": cliente_selecionado,
        "pets": pets,
        "consultas": consultas
    }
    return render(requet, "clientes/detalhar_cliente.html", context)


@login_required()
def cadastar_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            cpf = form_cliente.cleaned_data["cpf"]
            email = form_cliente.cleaned_data["email"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            profissao = form_cliente.cleaned_data["profissao"]
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = enderecos_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, cpf=cpf, email=email, data_nascimento=data_nascimento,
                                               profissao=profissao, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar-clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()

    context = {
        "form_cliente": form_cliente,
        "form_endereco": form_endereco
    }
    return render(request, "clientes/form_cliente.html", context)


@login_required()
def editar_cliente(request, id):
    cliente_antigo = cliente_service.get_cliente(id)
    endereco_antigo = enderecos_service.get_endereco(cliente_antigo.endereco.id)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_antigo)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco_antigo)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data["nome"]
        cpf = form_cliente.cleaned_data["cpf"]
        email = form_cliente.cleaned_data["email"]
        data_nascimento = form_cliente.cleaned_data["data_nascimento"]
        profissao = form_cliente.cleaned_data["profissao"]
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_atualizado = enderecos_service.editar_endereco(endereco_antigo, endereco_novo)
            cliente_novo = cliente.Cliente(nome=nome, cpf=cpf, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, endereco=endereco_atualizado)
            cliente_service.editar_cliente(cliente_antigo, cliente_novo)
            return redirect('listar-clientes')

    context = {
        "form_cliente": form_cliente,
        "form_endereco": form_endereco
    }
    return render(request, "clientes/form_cliente.html", context)


@login_required()
def remover_cliente(request, id):
    cliente_selecionado = cliente_service.get_cliente(id)
    endereco_cliente = enderecos_service.get_endereco(cliente_selecionado.endereco.id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente_selecionado)
        enderecos_service.remover_endereco(endereco_cliente)
        return redirect('listar-clientes')

    context = {
        "cliente": cliente_selecionado
    }
    return render(request, "clientes/remover_cliente.html", context)
