from django.contrib import admin
from . models import Sang,Donateur,Stock,Hopitaux, Commande
from .forms import StockCreateForm, DonateurCreateForm, HopitauxCreateForm, CommandeCreateForm

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['description', 'stock_groupe', 'quantite']
   form = StockCreateForm
   list_filter = ['stock_groupe']
   search_fields = ['stock_groupe']

class DonateurCreateAdmin(admin.ModelAdmin):
   list_display = ['nom', 'groupe_sanguin', 'genre', 'tel', 'adresse']
   form = DonateurCreateForm
   list_filter = ['groupe_sanguin']
   search_fields = ['groupe_sanguin']

class HopitauxCreateAdmin(admin.ModelAdmin):
   list_display = ['nom', 'adress', 'tel', 'email']
   form =HopitauxCreateForm
   list_filter = ['nom']
   search_fields = ['nom']

class CommandeCreateAdmin(admin.ModelAdmin):
   list_display = ['partenaire', 'groupe_sanguin', 'quantite_commande']
   form = CommandeCreateForm
   list_filter = ['groupe_sanguin']
   search_fields = ['partenaire']

admin.site.register(Sang)
admin.site.register(Hopitaux, HopitauxCreateAdmin)
admin.site.register(Commande, CommandeCreateAdmin)
admin.site.register(Donateur, DonateurCreateAdmin)
admin.site.register(Stock, StockCreateAdmin)
