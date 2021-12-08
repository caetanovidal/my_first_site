from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Features, Movel, FotoProduto


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature', 'descricao', 'icone', 'ativo', 'modificado')


@admin.register(Movel)
class MovelAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'ativo', 'modificado')


@admin.register(FotoProduto)
class Foto_ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ativo', 'modificado')






