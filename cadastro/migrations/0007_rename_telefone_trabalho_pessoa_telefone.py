# Generated by Django 5.0.4 on 2024-04-16 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_remove_pessoa_acesso_direitos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='telefone_trabalho',
            new_name='telefone',
        ),
    ]
