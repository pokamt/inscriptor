from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import Universite
# from .forms import CandidatForm

"""
def index(request):
    data = {'test': 'le testeur de les choses'}
    return render (request, 'index.html', data)
"""
def index(request):
	return render (request, "index.html")
	# if request.method == 'POST':
	# 	f = CandidatForm(request.POST or None)
	# 	if f.is_valid():
	# 		f.save()
	# 		messages.success(request, ('Votre demande de participation est bien pris en compte, vous allez recevoir un message d\'information à ce propos, consultez votre boite aux lettres'))
	# 		return redirect('succes.html')
	# else:
	# 	data = {'universite' : Universite.objects.all, 'formulaire' : CandidatForm()}
	# 	return render(request, "index.html")
def info(request):
	return render (request, "info.html")

def condition(request):
	return render (request, "condition.html")