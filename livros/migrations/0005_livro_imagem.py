# Generated by Django 5.1.4 on 2025-01-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='livros/'),
        ),
    ]
