from django import forms
from .models import Stock, Donateur, Hopitaux, Commande
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['description', 'stock_groupe', 'quantite']

class CommandeCreateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['partenaire', 'groupe_sanguin', 'quantite_commande']

class DonateurCreateForm(forms.ModelForm):
    class Meta:
        model = Donateur
        fields = ['nom', 'groupe_sanguin', 'genre', 'tel', 'adresse']

class HopitauxCreateForm(forms.ModelForm):
    class Meta:
        model = Hopitaux
        fields = ['nom', 'adress', 'tel', 'email']

class CreateUserForm(UserCreationForm):
    class Meta:
	    model = User
	    fields = ['username', 'email', 'password1', 'password2']   