# Generated by Django 3.2.7 on 2021-09-16 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('nascimento', models.DateField(verbose_name='Data nascimento')),
                ('categoria', models.CharField(choices=[('Cachorro', 'Cachorro'), ('Gato', 'Gato'), ('Hamster', 'Hamster'), ('Coelho', 'Coelho')], max_length=10, verbose_name='Categoria')),
                ('cor', models.CharField(choices=[('Preto', 'Preto'), ('Branco', 'Branco'), ('Cinza', 'Cinza'), ('Marrom', 'Marrom'), ('Amarelo', 'Amarelo')], max_length=10, verbose_name='Cor')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]
