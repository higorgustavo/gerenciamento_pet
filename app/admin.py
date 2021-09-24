from django.contrib import admin
from .models import Cliente, Endereco, Pet, Consulta, Funcionario


admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Pet)
admin.site.register(Consulta)
admin.site.register(Funcionario)
