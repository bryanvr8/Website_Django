from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cpf_cliente', 'endereco_cliente', 'cidade_cliente', 'estado_cliente')