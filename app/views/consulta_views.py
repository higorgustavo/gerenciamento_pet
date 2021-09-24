from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from ..entidades import consulta
from ..services import pet_service, consulta_service
from ..forms.consulta_form import ConsultaForm
from gerenciamento_pet import settings


@user_passes_test(lambda usuario: usuario.cargo == 1)
def cadastrar_consulta(request, id):
    if request.method == "POST":
        form_consulta = ConsultaForm(request.POST)
        pet = pet_service.get_pet(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data['motivo_consulta']
            peso_atual = form_consulta.cleaned_data['peso_atual']
            medicamento_atual = form_consulta.cleaned_data['medicamento_atual']
            medicamentos_prescritos = form_consulta.cleaned_data['medicamentos_prescritos']
            exames_prescritos = form_consulta.cleaned_data['exames_prescritos']
            consulta_nova = consulta.Consulta(pet=pet, motivo_consulta=motivo_consulta, peso_atual=peso_atual,
                                              medicamento_atual=medicamento_atual,
                                              medicamentos_prescritos=medicamentos_prescritos,
                                              exames_prescritos=exames_prescritos)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('detalhar-pet', pet.id)

    else:
        form_consulta = ConsultaForm()

    context = {
        "form_consulta": form_consulta
    }
    return render(request, "consultas/form_consulta.html", context)


@login_required()
def detalhar_consulta(request, id):
    consulta_selecionada = consulta_service.get_consulta(id)
    context = {
        "consulta": consulta_selecionada
    }
    return render(request, "consultas/detalhar_consulta.html", context)


@login_required()
def enviar_email_consulta(request, id):
    consulta_selecionada = consulta_service.get_consulta(id)
    pet_selecionado = pet_service.get_pet(consulta_selecionada.pet.id)
    context = {
        "consulta": consulta_selecionada
    }
    assunto = "Resumo da consulta do seu Pet"
    conteudo_html = render_to_string("consultas/email_consulta.html", context)
    corpo_email = "Resumo da sia consulta"
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_selecionado.dono.email]
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=conteudo_html)
    return redirect('detalhar-consulta', id)
