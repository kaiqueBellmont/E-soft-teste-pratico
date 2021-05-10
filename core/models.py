from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    idade = models.PositiveIntegerField('Idade')
    data_nascimento = models.DateField('data de nascimento')
    email = models.EmailField('email', max_length=200, help_text='insira o email no formato example@example.com')
    apelido = models.CharField('apelido', max_length=100)
    observacao = models.TextField('Observações', help_text='observações gerais')

    def __str__(self):
        return self.nome
