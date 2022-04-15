from django.contrib import admin
from .models import Receitas, Ingredientes, QuantidadeIngredientes, Mensagens, TipoReceita
# Register your models here.

admin.site.register(Receitas)
admin.site.register(Ingredientes)
admin.site.register(QuantidadeIngredientes)
admin.site.register(Mensagens)
admin.site.register(TipoReceita)