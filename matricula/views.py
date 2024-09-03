from django.shortcuts import render
from matricula.forms import AlunoForm
from .models import *
# Create your views here.
def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()
    
    return render(request, 'form.html', {'form' : form})

def index(request):
    lista = Aluno.objects.all()
    return render(request, 'index.html', {'lista' : lista})