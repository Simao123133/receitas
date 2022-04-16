from django import forms
from .models import Receitas, QuantidadeIngredientes, Ingredientes
from django.contrib.auth.models import User 
from django.forms import inlineformset_factory
from django.utils import timezone



class CreateReceitasForm(forms.ModelForm):
    
    class Meta:
        model = Receitas
        fields = ['receita', 'ingredientes', 'procedimento', 'tipo', 'foto']

    def __init__(self, *args, **kwargs):
        super(CreateReceitasForm, self).__init__(*args, **kwargs)
        self.fields['foto'].required = False

    receita = forms.CharField(max_length=100)
    procedimento = forms.CharField(widget = forms.Textarea)
    foto = forms.ImageField()

    ingredientes = forms.ModelMultipleChoiceField(
        queryset=QuantidadeIngredientes.objects.filter(time_added__gte=timezone.now() - timezone.timedelta(hours=1)),
        widget=forms.CheckboxSelectMultiple
    )

class CreateQuantidadeIngredientesForm(forms.ModelForm):

    class Meta:
        model = QuantidadeIngredientes
        fields = ['ingrediente', 'quantidade']

class CreateIngredientesForm(forms.ModelForm):

    class Meta:
        model = Ingredientes
        fields = '__all__'






