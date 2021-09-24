from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_usuario(request):
    if request.method == "POST":
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('listar-clientes')
            else:
                messages.error(request, "As credenciais de usuário estão incorretas")
                return redirect('login')
    else:
        form_login = AuthenticationForm()

    context = {
        "form_login": form_login
    }
    return render(request, "autenticacao/login.html", context)


def logout_usuario(request):
    logout(request)
    return redirect('login')

