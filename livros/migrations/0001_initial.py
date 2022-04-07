# Generated by Django 4.0.3 on 2022-04-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('descricao', models.CharField(max_length=400)),
                ('editora', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
