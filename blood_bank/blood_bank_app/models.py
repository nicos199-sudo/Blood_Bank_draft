from django.db import models
from django.contrib.auth.models import User


class Sang(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Donateur(models.Model):
    GENRE_CHOICES= [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
    ]

    nom = models.CharField(max_length=30)
    groupe_sanguin = models.ForeignKey(Sang, null=True, on_delete= models.SET_NULL)
    tel = models.CharField(max_length=30)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    nationalite = models.CharField(max_length=20)
    age = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Stock(models.Model):
    stock_groupe = models.ForeignKey(Sang, null=True, on_delete = models.SET_NULL)
    quantite = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.description

class Hopitaux(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Commande(models.Model):
	partenaire = models.ForeignKey(Hopitaux, null=True, on_delete= models.SET_NULL)
	groupe_sanguin = models.ForeignKey(Sang, null=True, on_delete= models.SET_NULL)
	date_commande = models.DateTimeField(auto_now_add=True, null=True)
	quantite_commande = models.IntegerField()

	def __str__(self):
    		return self.partenaire.nom

