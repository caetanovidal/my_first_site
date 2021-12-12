from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .models import Servico, Funcionario, Features, Movel, FotoProduto
from .forms import ContatoForm
from django.urls import reverse_lazy
from  django.contrib import messages
# Create your views here.


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['features'] = Features.objects.all()
        context['moveis'] = Movel.objects.all()
        context['fotos_produtos'] = FotoProduto.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class MoveisView(TemplateView):
    template_name = 'moveis.html'






"""
class TesteView(TemplateView):
    template_name = '404.html'
    

<QuerySet [<Features: Entrega Rápida>, <Features: Computadores e Celulares>, <Features: Diversas Plataformas>, <Features: Design Moderno>, <Features: Múltiplas Funções>, <Features: Ecologicamente Incorreto>]>
"""
