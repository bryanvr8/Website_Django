from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=20, null=False)
    cpf_cliente = models.CharField(max_length=11, null=False)
    endereco_cliente = models.CharField(max_length=100, null=False)
    cidade_cliente = models.CharField(max_length=10, null=False)
    estado_cliente = models.CharField(max_length=6, null=False)
