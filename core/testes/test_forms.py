from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Adriano Robson'
        self.email = 'Adriano@gmail.com'
        self.assunto = 'Assunto do email'
        self.mensagem = 'Teste para o formulário de envio de email'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        # Aqui estamos fazendo uma simulação de um POST, ContatoFOrm(request.POST)
        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):

        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        # Verificando se o retorno do res1 é igual o res2
        self.assertAlmostEquals(res1, res2)