from django.contrib import admin

from .models import Pessoa


@admin.register(Pessoa)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao')
