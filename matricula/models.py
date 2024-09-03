from django.db import models

# Create your models here.
class Aluno(models.Model):
    Nome = models.CharField(max_length=60)
    Endereco = models.CharField(max_length=150)
    Cidade = models.CharField(max_length=100)
    Email = models.EmailField(max_length=150)
    Curso = models.CharField(max_length=180)
    
    def __str__(self):
        return self.Nome