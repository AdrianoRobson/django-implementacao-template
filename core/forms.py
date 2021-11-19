from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        content = f'Nome: {nome}\n'\
            f'E-mail: {email}\n'\
            f'Assunto: {assunto}\n'\
            f'Mensagem: {mensagem}'
        
        mail =EmailMessage(
            subject=assunto,
            body=content,
            from_email='teste@template.com.br',
            to=['teste2@template.com.br'],
            headers={'Replay-To: ': email}
        )

        mail.send()