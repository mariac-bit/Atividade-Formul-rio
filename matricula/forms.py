from django import forms
from matricula.models import Aluno
class AlunoForm(forms.ModelForm):
    
    class Meta:
        model=Aluno
        fields = '__all__'
        