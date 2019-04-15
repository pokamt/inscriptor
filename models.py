from django.db import models

class Universite(models.Model):
	nom = models.CharField(max_length=200)
	adresse = models.CharField(max_length=200)

	def __str__(self):
		return self.nom
		
class Candidat(models.Model):
	"""Classe permettant d'eregistrer toutes les candidatures des doctrants"""
	nom = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	universite = models.ForeignKey(Universite, on_delete = models.CASCADE)
	filiere = models.CharField(max_length=200)
	theme = models.TextField()

	def __str__(self):
		return self.nom