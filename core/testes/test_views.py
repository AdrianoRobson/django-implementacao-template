from django.test import TestCase
from django.test import Client # GET, POST, PUT, DELETE, Client http
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Adriano Robson',
            'email': 'Adriano08Andrade@gmail.com',
            'assunto': 'Teste da view',
            'mensagem': 'Mensagem para teste da view'
        }
        self.cliente = Client()
    
    def test_form_valid(self):

        # Aplicando um post para a rota passando os dados
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        
        # Em http o redirect é representado pelo código 302
        self.assertEquals(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Adriano Robson',
            'assunto': 'Teste de view'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
