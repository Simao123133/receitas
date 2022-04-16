"""receitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 


app_name = 'receitas_app'

urlpatterns = [
    path('create_receitas/',views.ReceitasCreate.as_view(),name='create_receitas'),
    path('receitas/<int:pk>/',views.ReceitasDetail.as_view(),name='receitas_detail'),
    path('receitas_update/<int:pk>/',views.ReceitasUpdateView.as_view(),name='receitas_update'),
    path('create_ingredientes/',views.IngredientesCreate.as_view(),name='create_ingredientes'),
    path('create_quantidadeingredientes/',views.QuantidadeIngredientesCreate.as_view(),name='create_quantidadeingredientes'),
    path('ingredientes/<int:pk>/',views.IngredientesDetail.as_view(),name='ingredientes_detail'),
    path('',views.ReceitasList.as_view(),name='list_receitas'),
    path('refeicoes_list/',views.RefeicoesList.as_view(),name='list_refeicoes'),
    path('sobremesas_list/',views.SobremesasList.as_view(),name='list_sobremesas'),
    path('ingredientes_list/',views.IngredientesList.as_view(),name='list_ingredientes'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('success_login/',views.LoginView.as_view(),name='login_success'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_mensagens/',views.MensagensCreate.as_view(),name='create_mensagens'),
    path('success_message/',views.MensagemEnviadaView.as_view(),name='message_success'),
    path('both_forms',views.BothForms.as_view(),name='both_forms'),
    
]