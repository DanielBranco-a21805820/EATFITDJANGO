import uuid
from django.forms import ModelForm
from django.db import models
from multiselectfield import MultiSelectField


class BD(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    telemovel = models.IntegerField(default=000000000)
    email = models.EmailField(blank=False)
    nascimento = models.DateField(blank=False)

    def __str__(self):
        return f"{self.nome} {self.apelido}"


BRACOS = [
    ("lunges", "Lunges"),
    ("prancha", "Prancha"),
    ("fundos", "Fundos"),
    ("curls", "Bicep Curls"),
    ("ups", "Chin-ups"),
]


class Quizz(models.Model):
    pergunta1 = models.CharField(max_length=50)
    pergunta2 = models.CharField(max_length=50)
    pergunta3 = models.CharField(max_length=50)
    pergunta4 = models.CharField(max_length=50)
    pergunta5 = MultiSelectField(max_length=50, max_choices=5, choices=BRACOS)
    pergunta6 = models.CharField(max_length=50)
    pergunta7 = models.CharField(max_length=50)
    pergunta8 = models.CharField(max_length=50)
    pergunta9 = models.CharField(max_length=50)
    pergunta10 = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    compreensao = models.IntegerField(default=0)
    rigor = models.IntegerField(default=0)
    facilidade_acesso = models.IntegerField(default=0)
    importante = models.IntegerField(default=0)
    complexidade = models.IntegerField(default=0)
    perguntas_quizz = models.IntegerField(default=0)
    amplitude = models.IntegerField(default=0)
    originalidade = models.IntegerField(default=0)
    aconselha = models.IntegerField(default=0)
    feedback = models.TextField(max_length=500, default=1)

    def __str__(self):
        return str(self.id)


USER_OPINIONS = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['compreensao', 'rigor', 'facilidade_acesso', 'importante', 'complexidade', 'perguntas_quizz',
                  'amplitude', 'originalidade', 'aconselha', 'feedback']


class QuizForm(ModelForm):
    class Meta:
        model = Quizz
        fields = ['pergunta1', 'pergunta2', 'pergunta3', 'pergunta4', 'pergunta5', 'pergunta6', 'pergunta7',
                  'pergunta8', 'pergunta9', 'pergunta10']


class Professor(models.Model):
    pnome = models.CharField(max_length=64)
    unome = models.CharField(max_length=64)

    def __str__(self):
        return f"Professor(a) {self.pnome} {self.unome}"


class Aulas(models.Model):
    professor = models.ForeignKey(Professor,
                                  on_delete=models.CASCADE,
                                  related_name="Professor")
    nome = models.CharField(max_length=64, default="")
    sala = models.CharField(max_length=64, default="")
    duracao = models.IntegerField(default=60)

    def __str__(self):
        return f"{self.nome} na sala {self.sala} com a duração de {self.duracao} minutos dada por {self.professor}"


class Alunos(models.Model):
    pnome = models.CharField(max_length=64)
    unome = models.CharField(max_length=64)
    aula = models.ManyToManyField(Aulas,
                                  blank=True,
                                  related_name="Aula")

    def __str__(self):
        return f"{self.pnome} {self.unome}."
