from django import forms
from .models import BD, Comment


# definir qual modelo será usado para fazer o formulario
class BDCreate(forms.ModelForm):
    class Meta:
        model = BD
        fields = '__all__'


USER_OPINIONS = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class CommentForms(forms.Form):
    compreensao = forms.CharField(label='O conteúdo no website é de clara compreensão? 1(pouca) 5(muita):',
                                  widget=forms.RadioSelect(choices=USER_OPINIONS))
    rigor = forms.CharField(label='Como classifica o rigor da página? 1(pouca) 5(muita):',
                            widget=forms.RadioSelect(choices=USER_OPINIONS))
    facilidade_acesso = forms.CharField(
        label='É fácil aceder aos menus da página (multimedia, Informação,..) 1(pouca) 5(muita):',
        widget=forms.RadioSelect(choices=USER_OPINIONS))
    importante = forms.CharField(label='Sobre a informação apresentada, ela foca-se no importante 1(pouca) 5(muita):',
                                 widget=forms.RadioSelect(choices=USER_OPINIONS))
    complexidade = forms.CharField(label='O website está complexo e com multiplas inter-relacões 1(pouca) 5(muita):',
                                   widget=forms.RadioSelect(choices=USER_OPINIONS))
    perguntas_quizz = forms.CharField(label='As perguntas no quizz eram percetiveis? 1(pouca) 5(muita):',
                                      widget=forms.RadioSelect(choices=USER_OPINIONS))
    amplitude = forms.CharField(label='Quão amplo está o website? 1(pouca) 5(muita):',
                                widget=forms.RadioSelect(choices=USER_OPINIONS))
    originalidade = forms.CharField(label='O website está original? 1(pouca) 5(muita):',
                                    widget=forms.RadioSelect(choices=USER_OPINIONS))
    aconselha = forms.CharField(label='Aconselhava o site a outras pessoas? 1(pouca) 5(muita):',
                                widget=forms.RadioSelect(choices=USER_OPINIONS))
    feedback = forms.CharField(
        label='Diga-nos a sua opinião geral sobre o site e se tiver, faça aqui as suas sugestões para poder-mos melhorar',
        widget=forms.Textarea())


FERGUSON = [
    ( "real","Real Madrid"),
    ("chelsea", "Chelsea"),
    ("manu", "Manchester United"),
    ("celtic", "Celtic"),
]

NEDVED = [
    ("ajax", "Ajax"),
    ("chelsea", "Chelsea"),
    ("atleti", "Atlético Madrid"),
    ("juve", "Juventus"),
]

MESSI = [
    ("messi", "Messi"),
    ("zlatan", "Zlatan Ibrahimovic"),
    ("ronaldo", "Cristiano Ronaldo"),
    ("ronaldinho", "Ronaldinho"),
]

SENNA = [
    ("golf", "Golf"),
    ("surf", "Surf"),
    ("f1", "Fórmula 1"),
    ("ténis", "Ténis"),
]

EVORA = [
    ("100", "100m"),
    ("dardo", "Lançamento do dardo"),
    ("triplo", "Triplo Salto"),
    ("maratona", "Maratona"),
]

MARATONA = [
    ("agostinho", "Joaquim Agostinho"),
    ("lopes", "Carlos Lopes"),
    ("mamede", "Fernando Mamede"),
    ("pinto", "António Pinto"),
]

BRACOS = [
    ("lunges", "Lunges"),
    ("prancha", "Prancha"),
    ("fundos", "Fundos"),
    ("curls", "Bicep Curls"),
    ("ups", "Chin-ups"),
]

SUPERALIMENTO = [
    ("spirulina", "Espirulina"),
    ("gengibre", "Gengibre"),
    ("chocolate", "Chocolate"),
    ("goji", "Goji"),
]

SN = [
    ("sim", "Sim"),
    ("nao", "Não"),
]

LESAO = [
    ("gelo", "Gelo"),
    ("quente", "Quente"),
]

class QuizForms(forms.Form):
    pergunta1 = forms.CharField(label='Para perder peso devo ter uma dieta que me proporcione um défice calórico?',
                                  widget=forms.Select(choices=SN))
    pergunta2 = forms.CharField(label='Alex Ferguson foi treinador de que clube?',
                                  widget=forms.RadioSelect(choices=FERGUSON))
    pergunta3 = forms.CharField(label='Em qual destes clubes se destacou Pavel Nedved?',
                                widget=forms.RadioSelect(choices=NEDVED))
    pergunta4 = forms.CharField(label='Qual destes futebolistas ganhou 4 bolas de ouro seguidas?',
                                widget=forms.RadioSelect(choices=MESSI))
    pergunta5 = forms.MultipleChoiceField(label='Destes exercícios, selecione os exercícios de braços?',
                                choices=BRACOS, widget=forms.CheckboxSelectMultiple)
    pergunta6 = forms.CharField(label='Em que modalidade se destacou Ayrton Senna?',
                                widget=forms.RadioSelect(choices=SENNA))
    pergunta7 = forms.CharField(label='Qual o intruso nesta lista?',
                                widget=forms.RadioSelect(choices=SUPERALIMENTO))
    pergunta8 = forms.CharField(label='Em que especialidade de atletismo se destacou Nelson Évora?',
                                widget=forms.RadioSelect(choices=EVORA))
    pergunta9 = forms.CharField(label='O que devemos aplicar quando nos acabámos de lesionar?',
                                widget=forms.Select(choices=LESAO))
    pergunta10 = forms.CharField(label='Quem foi o vencedor da maratona nos Jogos Olímpicos de 1984?',
                                widget=forms.RadioSelect(choices=MARATONA))