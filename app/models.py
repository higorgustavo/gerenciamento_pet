from django.contrib.auth.models import AbstractUser
from django.db import models
from django_localflavor_br.br_states import STATE_CHOICES


class Endereco(models.Model):
    rua = models.CharField("Rua", max_length=100)
    cidade = models.CharField("Cidade", max_length=50)
    estado = models.CharField("Estado", max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return self.rua


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    cpf = models.CharField("CPF", max_length=14)
    data_nascimento = models.DateField("Data de Nascimento")
    profissao = models.CharField("Profissão", max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    CATEGORIA_PET_CHOICES = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Hamster', 'Hamster'),
        ('Coelho', 'Coelho'),
    )

    COR_PET_CHOICES = (
        ('Preto', 'Preto'),
        ('Branco', 'Branco'),
        ('Cinza', 'Cinza'),
        ('Marrom', 'Marrom'),
        ('Amarelo', 'Amarelo'),
    )
    nome = models.CharField("Nome", max_length=50)
    nascimento = models.DateField("Data nascimento")
    categoria = models.CharField("Categoria", max_length=10, choices=CATEGORIA_PET_CHOICES)
    cor = models.CharField("Cor", max_length=10, choices=COR_PET_CHOICES)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " - " + self.dono.nome


class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    data = models.DateField("Data da consulta", auto_now_add=True)
    motivo_consulta = models.CharField("Motivo da consulta", max_length=250)
    peso_atual = models.FloatField("Peso atual")
    medicamento_atual = models.TextField(null=False, blank=True)
    medicamentos_prescritos = models.TextField(null=False, blank=True)
    exames_prescritos = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.pet.nome + " - " + str(self.data)


class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField("Nome", max_length=50)
    nascimento = models.DateField("Data de nascimento")
    cargo = models.IntegerField("Cargo", choices=CARGO_CHOICES, null=False, blank=False)
