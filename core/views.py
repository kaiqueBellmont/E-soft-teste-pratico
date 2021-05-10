import datetime

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import requests
import json

from .models import Pessoa
from django.urls import reverse_lazy


class IndexView(ListView):
    models = Pessoa
    template_name = 'index.html'
    queryset = Pessoa.objects.order_by('nome').all()
    context_object_name = 'pessoas'


class CreatePessoaView(CreateView):
    model = Pessoa
    template_name = 'Pessoa_form.html'
    fields = ['nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao']
    success_url = reverse_lazy('index')

    def __init__(self, *args, **kwargs):
        super(CreatePessoaView, self).__init__(*args, **kwargs)

        request = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
        teste = json.loads(request.content)
        nome = teste[0]
        sobrenome = teste[1] + ' ' + teste[2]
        nome_completo = nome + ' ' + sobrenome

        self.initial['nome'] = nome
        self.initial['sobrenome'] = sobrenome
        self.initial['data_nascimento'] = datetime.date.today()


class UpdatePessoaView(UpdateView):
    model = Pessoa
    template_name = 'Pessoa_form.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class DeletePessoasView(DeleteView):
    model = Pessoa
    template_name = 'pessoa_del.html'
    success_url = reverse_lazy('index')

