from django.shortcuts import render
from django.shortcuts import render, redirect

from core.models import Presenca
from .forms import PresencaForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = PresencaForm(request.POST)
        if form.is_valid():
            presenca = form.save(commit=False)
            nome_professor = form.cleaned_data['nome_professor']
            presenca.nome_professor = nome_professor
            presenca.save()
            return redirect('cadastrar_presenca')
    else:
        form = PresencaForm()
    return render(request, 'cadastrar_presenca.html', {'form': form})

def listar_alunos(request):
    registros = Presenca.objects.all()
    return render(request, 'listar_presencas.html', {'registros': registros})

