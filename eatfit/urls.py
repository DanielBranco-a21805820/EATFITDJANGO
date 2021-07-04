from django.shortcuts import render
from django.urls import path
from django.conf.urls.static import static
from config.settings import STATIC_URL, MEDIA_URL, STATIC_ROOT, MEDIA_ROOT, DEBUG
from . import views

app_name = "eatfit"

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('batidos', views.batidos_page_view, name="batidos"),
    path('exercicios', views.exercicios_page_view, name="exercicios"),
    path('alimentos', views.alimentos_page_view, name="alimentos"),
    path('conselhos', views.conselhos_page_view, name="conselhos"),
    path('dietas', views.dietas_page_view, name="dietas"),
    path('website', views.website_page_view, name="website"),
    path('quizz', views.quizz_page_view, name="quizz"),
    path('formulario', views.formulario_page_view, name="contactos"),
    path('tabela', views.tabela_page_view, name="tabela"),
    path('comentarios', views.comentarios_page_view, name="comentarios"),
    path('resultados', views.resultados_page_view, name="resultados"),
    path('resultadosQuiz', views.resultadosQuiz_page_view, name="resultadosQuiz"),
    # TABELA
    path('<int:aula_id>', views.aula, name="aula"),
    path('taulas', views.taulas, name="taulas"),
    path('<int:aula_id>/inscrever', views.inscrever, name="inscrever"),
    # LOGIN
    path('login', views.login_page_view, name="login"),
    path('auth/', views.login_view, name="auth"),
    path('logout', views.logout_view, name="logout"),
    # BASE DE DADOS
    path('upload/', views.upload, name='contactos'),
    path('update/<int:eatandfit_id>', views.update_eatandfit, name='update'),
    path('delete/<int:eatandfit_id>', views.delete_eatandfit, name='delete'),
    # SPA
    path("autores", views.autores, name="autores"),
    path("sections/<int:num>", views.section, name="section")

]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
