from distutils.command.upload import upload
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.

class Ingredientes(models.Model):

    ingrediente = models.CharField(max_length=100)
    kcal = models.DecimalField(decimal_places=2, max_digits=10)
    proteinas = models.DecimalField(decimal_places=2, max_digits=10)
    hidratos = models.DecimalField(decimal_places=2, max_digits=10)
    gorduras = models.DecimalField(decimal_places=2, max_digits=10)
    unidade = models.CharField(max_length=100, default='g', blank=True)

    def __str__(self):
        return self.unidade + " " + self.ingrediente

    def get_absolute_url(self):
        return reverse("receitas_app:ingredientes_detail", kwargs={"pk": self.pk}) 

class QuantidadeIngredientes(models.Model):

    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    quantidade = models.DecimalField(default=1, decimal_places=2, max_digits=10)
    time_added = models.DateTimeField(auto_now=True)

    def __str__(self):

        return '%g'%(self.quantidade) + str(self.ingrediente)

class TipoReceita(models.Model):

    tipo = models.CharField(max_length = 30)

    def __str__(self):

        return str(self.tipo)

class Receitas(models.Model):

    receita = models.CharField(max_length=100)
    autor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    ingredientes = models.ManyToManyField(QuantidadeIngredientes)
    procedimento = models.TextField(max_length=300, default='Descrição')
    foto  = models.ImageField(null=True, blank=True, upload_to="", default='download_pr2ep5.jpg')
    tipo = models.ForeignKey(TipoReceita, on_delete=models.CASCADE,null=True)

    @property
    def kcal(self):
        
        return '%g'%(sum(ingrediente.quantidade*ingrediente.ingrediente.kcal for ingrediente in self.ingredientes.all()))

    @property
    def prot(self):
        return '%g'%(sum(ingrediente.quantidade*ingrediente.ingrediente.proteinas for ingrediente in self.ingredientes.all()))

    @property
    def hidr(self):
        return '%g'%(sum(ingrediente.quantidade*ingrediente.ingrediente.hidratos for ingrediente in self.ingredientes.all()))

    @property
    def gor(self):
        return '%g'%(sum(ingrediente.quantidade*ingrediente.ingrediente.gorduras for ingrediente in self.ingredientes.all()))

    def get_absolute_url(self):
        return reverse("receitas_app:receitas_detail", kwargs={"pk": self.pk})

    def get_change_url(self):
        return reverse("receitas_app:receitas_update", kwargs={"pk": self.pk})

    def __str__(self):

        return str(self.receita)
        

class Mensagens(models.Model):

    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=600, default='')

    def __str__(self):
        return self.primeiro_nome + self.segundo_nome 




    




