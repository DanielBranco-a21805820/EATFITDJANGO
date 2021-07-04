from django.contrib import admin
from eatfit.models import BD, Comment, Quizz, Alunos, Professor, Aulas


# Register your models here.
class AulasAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'professor',
                    'nome',
                    'sala',
                    'duracao')


class AlunoAdmin(admin.ModelAdmin):
    filter_horizontal = ('aula',)


admin.site.register(BD)
admin.site.register(Comment)
admin.site.register(Quizz)
admin.site.register(Aulas, AulasAdmin)
admin.site.register(Alunos, AlunoAdmin)
admin.site.register(Professor)
