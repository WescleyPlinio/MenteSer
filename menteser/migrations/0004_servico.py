# Generated by Django 5.2 on 2025-04-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteser', '0003_imagemindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('icone', models.CharField(max_length=100)),
            ],
        ),
    ]
