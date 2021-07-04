# Generated by Django 3.2.3 on 2021-07-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatfit', '0005_alunos_atividades_aulas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnome', models.CharField(max_length=64)),
                ('unome', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='alunos',
            name='atividade',
        ),
        migrations.RemoveField(
            model_name='aulas',
            name='codigo',
        ),
        migrations.AddField(
            model_name='alunos',
            name='aula',
            field=models.ManyToManyField(blank=True, related_name='Aula', to='eatfit.Aulas'),
        ),
        migrations.AddField(
            model_name='aulas',
            name='duracao',
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name='aulas',
            name='nome',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='aulas',
            name='sala',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.DeleteModel(
            name='Atividades',
        ),
    ]
