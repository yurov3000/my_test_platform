# Generated by Django 3.2.7 on 2022-01-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220113_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testbody',
            name='answers_1',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-1'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_10',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-10'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_2',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-2'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_3',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-3'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_4',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-4'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_5',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-5'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_6',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-6'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_7',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-7'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_8',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-8'),
        ),
        migrations.AlterField(
            model_name='testbody',
            name='answers_9',
            field=models.IntegerField(db_index=True, verbose_name='Ответ-9'),
        ),
    ]
