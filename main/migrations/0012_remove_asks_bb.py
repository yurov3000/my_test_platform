# Generated by Django 3.2.7 on 2021-11-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_answers_asks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asks',
            name='bb',
        ),
    ]
