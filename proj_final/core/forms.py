# forms.py
from django import forms
from .models import Presenca
from core import models

class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ('nome_aluno', 'nome_professor',) 


       
