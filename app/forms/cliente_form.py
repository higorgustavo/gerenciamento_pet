from django import forms
from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'data_nascimento', 'profissao']
        widgets = {
            'data_nascimento': forms.TextInput(attrs={
                'type': 'date'
            })
        }
