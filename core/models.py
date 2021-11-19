from typing import Sequence
from django.db import models
from stdimage.models import StdImageField
from django.db.models.signals import post_init, post_save, pre_delete
from django.dispatch.dispatcher import receiver
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('criação', auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Servico(Base):

    CHOISE_ICON = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )      

    servico = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=CHOISE_ICON)    
    delay_efeito = models.DecimalField("dalay-efeito", max_digits=2, decimal_places=1, default='1.0')
    
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('facebook', max_length=100, default='#')
    twitter = models.CharField('twitter', max_length=100, default='#')
    instagram = models.CharField('instagram', max_length=100, default='#')
    delay_efeito = models.DecimalField("dalay-efeito", max_digits=2, decimal_places=1, default='1.0')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
    

@receiver(pre_delete, sender=Funcionario)
def funcionario_pre(sender, instance, **kwargs): 
    instance.imagem.delete(False)  

@receiver(post_init, sender=Funcionario)
def funcionario_imagem(sender, instance, **kwargs): 
    instance.current_image_file = instance.imagem  

@receiver(post_save, sender=Funcionario)
def funcionario_change_image(sender, instance, **kwargs): 
    if hasattr(instance, 'current_image_file'): 
        if instance.imagem:
            if instance.current_image_file != instance.imagem:
                instance.current_image_file.delete(False)
            

    
