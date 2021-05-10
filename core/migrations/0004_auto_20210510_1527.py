# Generated by Django 2.2.8 on 2021-05-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210507_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(help_text='insira o email no formato example@example.com', max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.PositiveIntegerField(verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='observacao',
            field=models.TextField(help_text='observações gerais', verbose_name='Observações'),
        ),
    ]
