# Generated by Django 4.1.1 on 2022-09-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='number_check',
            field=models.CharField(default='ABC123', max_length=50, verbose_name='Номер предписания'),
        ),
        migrations.AddField(
            model_name='document',
            name='work_shift',
            field=models.CharField(choices=[('д', 'Дневная'), ('н', 'Ночная')], default='д', max_length=1, verbose_name='Рабочая смена'),
        ),
    ]