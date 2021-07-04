from django.shortcuts import render
from .models import BD, CommentForm, Comment, Quizz, QuizForm
from .forms import BDCreate, CommentForms, QuizForms
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .utils import get_plot, get_pie
from .calculator import solution


# Create your views here.

def home_page_view(request):
    return render(request, 'eatfit/home.html')


def batidos_page_view(request):
    nutricao = {
        "Batido de Chocolate e Menta": ["292 calorias", "25 g de proteína, 12 g de gordura", "32 g de carboidratos"],
        "Batido de Laranja e Baunilha": ["399 calorias, 32 g de proteína, 14 g de gordura, 39 g de carboidratos"],
        "Batido de Coco e Amêndoa": ["405  calorias, 27 g de proteína, 21 g de gordura, 33 g de carboidratos"],
        "Batido de Morango e Banana": [
            "489 calorias, 39 g de proteína, 11 g de gordura, 59 g de carboidratos, 7 g de fibra"],
    }

    ingredientes = {"Batido de Chocolate e Menta": ["1 colher de proteína de chocolate em pó",
                                                    "3/4 chávena de chocolate preto",
                                                    "1 colher de sopa de nozes",
                                                    "2 colheres de sopa de cacau em pó, não adoçado",
                                                    "1 colher de sopa de aparo de cacau", "2 folhas de menta",
                                                    "4 cubos de gelo",
                                                    "¼ copo de água"],
                    "Batido de Laranja e Baunilha": ["1 colher de pó de proteína de baunilha", "1 laranja",
                                                     "¼ casca de laranja", "1 colher de sopa de nozes",
                                                     "2 colheres de sopa de farinha de linhaça", "1 chávena de água",
                                                     "½ chávena de sumo de laranja",
                                                     "3 cubos de gelo"],
                    "Batido de Coco e Amêndoa": ["1 colher de proteína de chocolate em pó",
                                                 "1 colher de sopa de flocos de coco não adoçados",
                                                 "1 chávena de leite de amêndoas de seda, chocolate preto",
                                                 "1 colher de sopa redonda de manteiga de amêndoa",
                                                 "1½ água em chávenas", "3 cubos de gelo"],
                    "Batido de Morango e Banana": ["Água conforme a necessidade",
                                                   "1 chávena de kefir simples e magro",
                                                   "2 colheres de sopa de nozes",
                                                   "1 copo de morangos picados",
                                                   "1 banana", "1 colher de proteína de soro de baunilha"],

                    }
    imagem = {"Batido de Chocolate e Menta": "eatfit/images/batidochoc.png",
              "Batido de Laranja e Baunilha": "eatfit/images/batidolaran.png",
              "Batido de Coco e Amêndoa": "eatfit/images/batidococo.png",
              "Batido de Morango e Banana": "eatfit/images/batidomorango.png"}

    context = {
        'lista_n': nutricao,
        'ingredientes': ingredientes,
        'imagens': imagem
    }
    return render(request, 'eatfit/batidos.html', context)


def exercicios_page_view(request):
    return render(request, 'eatfit/exercicios.html')


def conselhos_page_view(request):
    cons11 = {"GELO": ["Acabou de se lesionar", "A zona magoada está inflamada", "Acabou de fazer exercício"],
              "QUENTE": ["A lesão é antiga", "Os músculos estão tensos", "Antes de fazer exercício"]
              }

    cons12 = {"GELO": "O propósito do gelo é reduzir a inflamação e minimizar o estrago que a lesão pode fazer",
              "QUENTE": "O calor ajuda a circulação e a mobilidade é melhor para a tensão muscular do que para uma lesão propriamente dita"
              }

    cons13 = {"GELO": "eatfit/images/gelo.png",
              "QUENTE": "eatfit/images/calor.png"
              }

    cons3 = ["Suporte muscular", "Remoção de congestionamento do fluxo de fluidos corporais",
             "Ativação do sistema analgésico endogénico", "Corrige problemas de juntas"]

    context = {
        'conselho11': cons11,
        'conselho12': cons12,
        'conselho13': cons13,
        'conselho3': cons3,
    }
    return render(request, 'eatfit/conselhos.html', context)


def dietas_page_view(request):
    perder = {
        "PROTEÍNAS": "A ingestão de proteínas saudáveis é muito importante, estas ajudam a manter a massa muscular e a aumentar a saciedade. ",
        "GORDURAS": "A ingestão de gorduras deve ser moderada e deve escolher fontes de gorduras saudáveis, as gorduras são nutrientes com um valor calórico mais elavdo, pelo que se deve ter cuidado com o que ingere.",
        "HIDRATOS DE CARBONO": "Deve consumir uma porção menor de hidratos de carbono. Normalmente não precisa de excluir estegrupo alimentar na totalidade, convém no entanto ajustar a dose consumida no dia-a-dia. Opte por ingerir hidratos de  carbono completos, pois estes tem uma absorção mais lenta, promovendo uma maior saciedade. Evite os  hidratos de carbono simples que são de absorção mais rápida, não dando tanta saciedade",
        "HIDRATAÇÃO": "Ingira entre 1.5 a 2 litros de água diariamente",
        "LEGUMES E FRUTAS": "Estes são boas fontes de fibra, vitaminas e minerais, são alimentos saudáveis que ajudam a saciar que apresentam níveis calóricos mais baixos, ter atenção no entanto com a fruta, esta é uma fonte de açúcar e por isso devem ser consumidas com alguma moderação",

    }

    ganhar = {
        "ALIMENTOS NUTRITIVOS": "Lá porque queremos ganhar peso não quer dizer que possamos comer tudo aquilo que queiramos. Deve-se manter uma dieta à base de alimentos que não sejam apenas saudáveis mas também nutritivos. Como por exemplo frango, aveia integral, carnes frescas, carboidratos e vegetais.",
        "MACRONUTRIENTES": "Para ganhar peso é importante ingerir quantidades adequadas dos três macronutrientes mais inportantes, são estes os hidratos de carbono, proteínas e gorduras boas. Eles devem estar presentes em todas as refeições do dia.",
        "PROTEÍNAS": "Estas são as responsáveis pela recuperação e desenvolvimento muscular, indispensáveis para quem treina. Estão normalmente presentes em maior quantidade na carne, peixe, ovos e quijo, sendo também possíveis consumir em alimentos de origem vegetal.",
        "GORDURAS": "Ajudam na absorção de vitaminas e fornecem energia, sendo encontradas no azeite, óleo de coco, nozes e amêndoas.",
        "HIDRATAÇÃO": "Manter-se hidratado é também muito importante, pois esta ajuda ao ganho de massa muscular, que apenas acontece se as células tiverem água para aumentar de volume.",

    }

    imagens_perder = {"PROTEÍNAS": "eatfit/images/xixa.png",
                      "GORDURAS": "eatfit/images/manteiga.png",
                      "HIDRATOS DE CARBONO": "eatfit/images/pao.png",
                      "HIDRATAÇÃO": "eatfit/images/agua.png",
                      "LEGUMES E FRUTAS": "eatfit/images/Abacate_e_Cenoura.png"}

    imagens_ganhar = {"ALIMENTOS NUTRITIVOS": "eatfit/images/corgete.png",
                      "MACRONUTRIENTES": "eatfit/images/ovo.png",
                      "PROTEÍNAS": "eatfit/images/peixe.png",
                      "GORDURAS": "eatfit/images/coconut.png",
                      "HIDRATAÇÃO": "eatfit/images/garrafa.png"}

    context = {
        'perder': perder,
        'imagens_perder': imagens_perder,
        'ganhar': ganhar,
        'imagens_ganhar': imagens_ganhar
    }

    return render(request, 'eatfit/dietas.html', context)


def alimentos_page_view(request):
    alimentos = {
        "GOJI": "São antioxidantes, ricas em proteínas, vitaminas e minerais. Fortalecem ainda osistema imunitário, reforçam a flora intestinal, diminuemos níveis de stress e retardam o envelhecimento das células. Podem ser consumidas em forma de passas, adicionadas ao iogurte, saladas, batidos ou como snacks. Mas atenção, não consuma em exagero... 10 a 15 bagas, cinco a seis vezes por semana é suficiente.",
        "SEMENTES DE CHIA": "São muito ricas em ácidos gordos essenciais (ómega-3 e 6), proteína e fibra, bem como vários minerais – cálcio, ferro, fósforo, selénio, potássio e manganésio. Podem ser consumidas em saladas, iogurtes ou com a água que bebe no dia-a-dia. dose diária aconselhável é de 2 colheres de sopa, divididas em pequenas porções nas diferentes refeições.",
        "SPIRULINA": "Esta alga de cor verde possui quantidades relevantes de proteína, vitamina B12, ferro, ómega-6 e antioxidantes como o betacaroteno. A sua propriedade, juntamente com a elevada capacidade antioxidante, fazem da spirulina um importante aliado para os desportistas, sobretudo no pós-treino, auxiliando na recuperação muscular. Semanalmente, a dose recomendada é de uma colher de chá, uma ou duas vezes por semana. Podendo ser adicionada a batidos, sumos, saladas e sopas.",
        "AVEIA": "Rica em fibras solúveis e insolúveis, a aveia promove o bom funcionamento intestinal e ajuda a reduzir os níveis de colesterol. Devido ao seu índice glicémico moderado, que estabiliza os níveis de glicémia e insulina, ajuda na perda de peso. Cálcio, ferro, proteínas, vitaminas do grupo B e E e hidratos de carbono são as grandes mais-valias deste superalimento. As papas de aveia são a sua forma mais comum e é ideal para pequeno-almoço. Pode ainda ser adicionada a iogurtes ou batidos..",
        "ABACATE": "O abacate tem um elevado poder de saciar e por ser rico em ácido oleico, aumenta o bom colesterol (HDL) e diminui o mau (LDL). No entanto, por ser uma fruta muito calórica e com muita gordura, deverá ser consumida em pequenas quantidades nas dietas de emagrecimento. Uma a duas vezes por semana será o suficiente em saladas, na confeção de molhos ou mesmo sozinho",
    }
    imagens = {"GOJI": "eatfit/images/goji.png",
               "SEMENTES DE CHIA": "eatfit/images/chia.png",
               "SPIRULINA": "eatfit/images/spirulina.png",
               "AVEIA": "eatfit/images/aveia.png",
               "ABACATE": "eatfit/images/abacate.png"}
    context = {
        'alimentos': alimentos,
        'imagens': imagens
    }
    return render(request, 'eatfit/alimentos.html', context)


def website_page_view(request):
    return render(request, 'eatfit/website.html')


def quizz_page_view(request):
    fields = ['pergunta1', 'pergunta2', 'pergunta3', 'pergunta4', 'pergunta5', 'pergunta6', 'pergunta7', 'pergunta8',
              'pergunta9', 'pergunta10']
    respostas = []
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            for pergunta in fields:
                respostas.append(form.cleaned_data[pergunta])
            request.session['respostas'] = respostas
            return HttpResponseRedirect(reverse('eatfit:resultadosQuiz'))
    form = QuizForms

    context = {
        'form': form,
    }

    return render(request, 'eatfit/quizz.html', context)


def resultadosQuiz_page_view(request):
    respostas = request.session.get('respostas')
    resultado = solution(respostas)
    erradas = 10 - resultado[0]
    chart = get_pie(resultado[0], erradas)
    context = {
        'pontos': resultado[0],
        'perguntas': resultado[1],
        'chart': chart
    }

    return render(request, 'eatfit/resultadosQuiz.html', context)


def comentarios_page_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eatfit:home'))

    form = CommentForms
    context = {
        'form': form
    }
    return render(request, 'eatfit/comentarios.html', context)


def resultados_page_view(request):
    resComments = Comment.objects.all()
    fields = ['compreensao', 'rigor', 'facilidade_acesso', 'importante', 'complexidade', 'perguntas_quizz', 'amplitude',
              'originalidade', 'aconselha']
    medias = []

    for x in fields:
        soma = 0
        list_a = list(resComments.values_list(x))
        for valor in list_a:
            soma += int(valor[0])
        medias.append(soma / resComments.count())

    chart = get_plot(fields, medias)
    return render(request, 'eatfit/resultados.html', {'chart': chart})


def formulario_page_view(request):
    return render(request, 'eatfit/contactos.html')


# Login

def login_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('eatfit:auth'))
    else:
        return HttpResponseRedirect(reverse('eatfit:tabela'))


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('eatfit:tabela'))
        else:
            return render(request, 'eatfit/login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'eatfit/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'eatfit/login.html', {
        'message': 'Logged out'})


# BASE DE DADOS
def tabela_page_view(request):
    context = {'lista': BD.objects.all()}
    return render(request, 'eatfit/tabela.html', context)


def upload(request):
    form = BDCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('eatfit:home'))

    context = {'form': form}

    return render(request, 'eatfit/contactos.html', context)


def update_eatandfit(request, eatandfit_id):
    bd = BD.objects.get(id=eatandfit_id)
    form = BDCreate(request.POST or None, instance=bd)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('eatfit:tabela'))

    context = {'form': form, 'user_id': eatandfit_id}
    return render(request, 'eatfit/update.html', context)


def delete_eatandfit(request, eatandfit_id):
    BD.objects.get(id=eatandfit_id).delete()
    return HttpResponseRedirect(reverse('eatfit:tabela'))


# Tabela
from .models import Professor, Alunos, Aulas


def taulas(request):
    context = {'aulas': Aulas.objects.all()}
    return render(request, 'eatfit/taulas.html', context)


def aula(request, aula_id):
    a = Aulas.objects.get(pk=aula_id)
    context = {'Aula': a,
               'alunos': a.Aula.all(),
               'non_alunos': Alunos.objects.exclude(aula=a),
               }
    return render(request, 'eatfit/aula.html', context)


def inscrever(request, aula_id):
    if request.method == "POST":
        a = Aulas.objects.get(pk=aula_id)
        aluno = Alunos.objects.get(pk=int(request.POST["aluno"]))
        aluno.aula.add(a)
        return HttpResponseRedirect(reverse('eatfit:aula', args=(a.id,)))



texts = [("<h3>Daniel Branco</h3> <p>Um desportista nato. Já praticou um leque bastante variado de desportos. Neste momento treina por conta própria, focando-se no treino funcional e de força no ginásio ou em casa. Leva um estilo de vida saudável.</p>"), ("<h3>Elisa Morgado</h3> <p>Praticante de desporto desde os 3 anos, começando por natação, evoluindo para o ténis e neste momento praticante de kung fu. Além disso também é praticante de uma boa alimentação saudável</p>")]


def autores(request):
    return render(request, "eatfit/autores.html")


def section(request, num):
    if 1 <= num <= 2:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")
