from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm
from time import sleep
import requests


def home(request):
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_dolar2 = cotacao_dolar + ";" + cotacao['USDBRL']['create_date']
    return render(request, 'index.html', {'cotacao_dolar': cotacao_dolar, 'data': cotacao_dolar2})


def cliente(request):
    return render(request, 'cliente.html')


def create(request):
    list = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR',
            'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

    nome_cliente = request.POST.get("nome_cliente")
    cpf_cliente = request.POST.get("cpf_cliente")
    endereco_cliente = request.POST.get("endereco_cliente")
    cidade_cliente = request.POST.get("cidade_cliente")
    estado_cliente = request.POST.get("estado_cliente")

    if (nome_cliente == '' or cpf_cliente == '' or endereco_cliente == '' or cidade_cliente == '' or estado_cliente == ''):
        messages.info(request, 'Preencha os campos abaixo por favor!')
        return redirect('/app/create/')
    else:

        if Cliente.objects.filter(cpf_cliente=cpf_cliente).exists():
            messages.info(
            request, 'CPF já cadastrado! Por favor tente novamente... ')
            return redirect('/app/create/')

        else:
            clientes = Cliente(
                nome_cliente=nome_cliente,
                cpf_cliente=cpf_cliente,
                endereco_cliente=endereco_cliente,
                cidade_cliente=cidade_cliente,
                estado_cliente=estado_cliente,
            )
            #clientes.save()
            return read_consult(request)


def read(request):
    read_all = Cliente.objects.all()
    return render(request, 'read.html', {'read_all': read_all})


def read_consult(request):
    read_last = Cliente.objects.last()
    return render(request, 'create.html', {'read_last': read_last})


def update(request, id):
    cliente = Cliente.objects.filter(id=id).first()
    form = ClienteForm(instance=cliente)

    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
        if (form.is_valid()):
            cliente.save()
            return redirect('/app/read/')
        else:
            return render(request, 'update.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'update.html', {'form': form, 'cliente': cliente})


def delete(request, id):
    delete_cliente = Cliente.objects.get(id=id)
    delete_cliente.delete()
    return read_consult(request)
