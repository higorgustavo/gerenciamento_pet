from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from ..forms.funcionario_forms import FuncionarioForm
from ..entidades import funcionario
from ..services import funcionario_service


@login_required()
def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    context = {
        'funcionarios': funcionarios
    }
    return render(request, 'funcionarios/listar_funcionarios.html', context)


@login_required()
def cadastrar_funcionario(request):
    if request.method == "POST":
        form_funcionario = FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data["nome"]
            nascimento = form_funcionario.cleaned_data["nascimento"]
            cargo = form_funcionario.cleaned_data["cargo"]
            username = form_funcionario.cleaned_data["username"]
            password = make_password(form_funcionario.cleaned_data["password1"])
            funcionario_novo = funcionario.Funcionario(nome=nome, nascimento=nascimento, cargo=cargo, username=username,
                                                       password=password)
            funcionario_service.cadastrar_funcionario(funcionario_novo)
            return redirect('listar-funcionarios')
    else:
        form_funcionario = FuncionarioForm()

    context = {
        'form_funcionario': form_funcionario
    }
    return render(request, 'funcionarios/form_funcionario.html', context)