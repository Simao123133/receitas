# Generated by Django 4.0.4 on 2022-04-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas_app', '0002_alter_receitas_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='foto',
            field=models.ImageField(blank=True, default='rojoes.jpeg', null=True, upload_to=''),
        ),
    ]
