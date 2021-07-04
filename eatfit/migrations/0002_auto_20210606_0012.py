# Generated by Django 3.2.3 on 2021-06-05 23:12

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eatfit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compreensao', models.IntegerField(default=0)),
                ('rigor', models.IntegerField(default=0)),
                ('facilidade_acesso', models.IntegerField(default=0)),
                ('importante', models.IntegerField(default=0)),
                ('complexidade', models.IntegerField(default=0)),
                ('perguntas_quizz', models.IntegerField(default=0)),
                ('amplitude', models.IntegerField(default=0)),
                ('originalidade', models.IntegerField(default=0)),
                ('aconselha', models.IntegerField(default=0)),
                ('feedback', models.TextField(default=1, max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='bd',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='pergunta5',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('lunges', 'Lunges'), ('prancha', 'Prancha'), ('fundos', 'Fundos'), ('curls', 'Bicep Curls'), ('ups', 'Chin-ups')], max_length=50),
        ),
    ]
