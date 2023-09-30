from django.db import models

class Aluno(models.Model):
    foto = models.ImageField(upload_to='foto')
    nome = models.CharField(max_length=25)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereço = models.CharField(max_length=70)
    cep = models.CharField(max_length=8)
    email = models.CharField(max_length=16)
    contato = models.CharField(max_length=12)

    def __str__(self):
        return self.nome
