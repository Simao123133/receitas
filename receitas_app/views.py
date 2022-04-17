from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 
from .forms import CreateReceitasForm, CreateQuantidadeIngredientesForm, CreateIngredientesForm, UpdateReceitasForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404

from receitas_app.models import Mensagens, Receitas, Ingredientes, QuantidadeIngredientes
# Create your views here.

class IngredientesCreate(LoginRequiredMixin,CreateView): #receitas_form.html
    model = Ingredientes
    fields = '__all__'
    success_url = reverse_lazy('receitas_app:create_receitas')

class QuantidadeIngredientesCreate(LoginRequiredMixin,CreateView): #receitas_form.html
    model = QuantidadeIngredientes
    fields = '__all__'
    success_url = reverse_lazy('receitas_app:create_receitas')

class ReceitasDetail(DetailView):
    model = Receitas

class IngredientesDetail(DetailView):
    model = Ingredientes

class ReceitasList(ListView):
    model = Receitas
    context_object_name = 'lista_receitas'

class RefeicoesList(ListView):
    model = Receitas
    context_object_name = 'lista_receitas'
    template_name = "receitas_app/receitas_list_refeicoes.html"

class SobremesasList(ListView):
    model = Receitas
    context_object_name = 'lista_receitas'
    template_name = "receitas_app/receitas_list_sobremesas.html"

class SignUpView(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'receitas_app/signup.html'

class LoginView(TemplateView):
    template_name = "receitas_app/login_success.html"

class MensagemEnviadaView(TemplateView):
    template_name = "receitas_app/message_success.html"

class MensagensCreate(CreateView): #receitas_form.html
    model = Mensagens
    fields = '__all__'
    success_url = reverse_lazy('receitas_app:message_success')

class ReceitasUpdateView(LoginRequiredMixin,UpdateView):
    model = Receitas
    form_class = UpdateReceitasForm
    template_name_suffix = "_update_form"
    

class IngredientesList(ListView):
    model = Ingredientes
    context_object_name = 'lista_ingredientes'

class ReceitasCreate(LoginRequiredMixin,CreateView): #receitas_form.html
    model = Receitas
    form_class = CreateReceitasForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
       
        return super().form_valid(form)

def _get_form(request, formcls, prefix):
    
    if prefix == 'aform_pre':

        return formcls(request.POST, request.FILES, prefix=prefix)
    
    data = request.POST if prefix in request.POST else None

    return formcls(data, prefix=prefix)

class BothForms(PermissionRequiredMixin,TemplateView):

    template_name = 'receitas_app/both_forms.html'

    permission_required = 'receitas_app.change_receitas'
    permission_denied_message = "Não tem permissão para criar receitas, enviar mensagem a pedir"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({'aform': CreateReceitasForm(prefix='aform_pre'), 'bform': CreateQuantidadeIngredientesForm(prefix='bform_pre'), 'cform': CreateIngredientesForm(prefix='cform_pre')})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        aform = _get_form(request, CreateReceitasForm, 'aform_pre')
        bform = _get_form(request, CreateQuantidadeIngredientesForm, 'bform_pre')
        cform = _get_form(request, CreateIngredientesForm, 'cform_pre')
        
        if aform.is_bound and aform.is_valid():
            aform.instance.autor = self.request.user
            aform.save()
            return redirect('receitas_app:list_receitas')

        elif bform.is_bound and bform.is_valid():
            bform.save()
            return redirect('receitas_app:both_forms')

        elif cform.is_bound and cform.is_valid():
            cform.save()
            return redirect('receitas_app:both_forms')    

        context = self.get_context_data(**kwargs)
        context.update({'aform': aform, 'bform': bform, 'cform': cform})

        return self.render_to_response(context)















    




