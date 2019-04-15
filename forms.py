from django import forms
from .models import Candidat, Universite

class CandidatForm(forms.ModelForm):
	"""
	nom = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-lg',
		}))

	email = forms.EmailField(widget=forms.EmailInput(
		attrs={
			'class': 'form-control form-control-lg',
		}))
	
	universite = forms.ModelChoiceField(queryset=Universite.objects.all(), widget=forms.Select(
		attrs={
			'class': 'form-control form-control-lg',
		}))
	
	filiere = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-lg',
		}))

	theme = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control form-control-lg',
		}))
	"""
	class Meta:
		model = Candidat
		fields = ["nom", "email", "filiere", "theme"]