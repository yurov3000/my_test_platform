# Generated by Django 3.2.7 on 2021-11-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211116_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asks',
            name='answers',
        ),
        migrations.AddField(
            model_name='asks',
            name='answer',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
        migrations.AddField(
            model_name='asks',
            name='text_answers',
            field=models.TextField(blank=True, max_length=50, verbose_name='Ответ'),
        ),
    ]