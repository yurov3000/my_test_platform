# Generated by Django 3.2.7 on 2022-01-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20220111_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='answers_10',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-10'),
        ),
        migrations.AddField(
            model_name='bb',
            name='answers_6',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-6'),
        ),
        migrations.AddField(
            model_name='bb',
            name='answers_7',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-7'),
        ),
        migrations.AddField(
            model_name='bb',
            name='answers_8',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-8'),
        ),
        migrations.AddField(
            model_name='bb',
            name='answers_9',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-9'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='answers_1',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-1'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='answers_2',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-2'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='answers_3',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-3'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='answers_5',
            field=models.CharField(blank=True, db_index=True, max_length=70, verbose_name='Ответ-5'),
        ),
    ]
