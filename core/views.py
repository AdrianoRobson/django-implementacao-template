from django.contrib.messages.api import success
from django.views.generic import FormView
from .models import Servico, Funcionario 
from .forms import ContatoForm  # Importanto o formulário de contato
from django.urls import reverse_lazy  # Para redirecionamento
from django.contrib import messages  # Para apresentação de mensagens no nosso template


class IndexView(FormView):

    template_name = 'index.html'

    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()   
        context['funcionarios'] = Funcionario.objects.order_by('?').all
        return context
    

    def form_valid(self, form, *args, **kwargs):
        form.send_mail() 
        messages.success(self.request, 'Email enviado')
        return super(IndexView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Houve um erro ao enviar!', extra_tags='danger')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
