from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField, proxy
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from .utilites import get_timestamp_path


# Модель пользователей
class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


# Рубрики
class Rubric(models.Model):
    name = CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = IntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_rubric = ForeignKey('SuperRubric', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тема')


# Модель надрубрик
class SuperRubricManager(models.Manager):  # Диспетчер записей станет выбирать только записи с пустым полем super_rubric
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=True)


class SuperRubric(Rubric):  # proxy-модель надрубрик
    object = SuperRubricManager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


# Модель подрубрик
class SubRubricManager(models.Manager):  # Диспетчер записей будет отбирать лишь записи с непустым полем
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=False)


class SubRubric(Rubric):  # proxy-модель подрубрик
    object = SubRubricManager()

    def __str__(self):
        return '%s - %s' % (self.super_rubric.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'Подтема'
        verbose_name_plural = 'Подтемы'


# модель самих объявлений
class Bb(models.Model):
    image = ImageField(upload_to=get_timestamp_path, blank=True, verbose_name='Изображения')
    author = ForeignKey(AdvUser, on_delete=CASCADE, verbose_name='Автор теста')
    is_active = BooleanField(db_index=True, default=True, verbose_name='Выводить в списке?')
    created_at = DateTimeField(db_index=True, auto_now_add=True, verbose_name='Опубликовано')

    rubric = ForeignKey('SubRubric', on_delete=models.PROTECT, verbose_name='Тема')
    title = CharField(max_length=40, verbose_name='Название темы')

    # answer = BooleanField(default=False, verbose_name='Правильный ответ')

    def delete(self, *args, **kwargs):
        for an in self.answers_set.all():
            an.delete()
        super().delete(*args, **kwargs)

    class Meta():
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
        ordering = ['-created_at']


class TestBody(models.Model):
    bb = ForeignKey('Bb', on_delete=models.PROTECT, verbose_name='Тест')

    ask_test_1 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_1 = IntegerField(db_index=True, verbose_name='Ответ-1')
    ask_test_2 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_2 = IntegerField(db_index=True, verbose_name='Ответ-2')
    ask_test_3 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_3 = IntegerField(db_index=True, verbose_name='Ответ-3')
    ask_test_4 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_4 = IntegerField(db_index=True, verbose_name='Ответ-4')
    ask_test_5 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_5 = IntegerField(db_index=True, verbose_name='Ответ-5')
    ask_test_6 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_6 = IntegerField(db_index=True, verbose_name='Ответ-6')
    ask_test_7 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_7 = IntegerField(db_index=True, verbose_name='Ответ-7')
    ask_test_8 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_8 = IntegerField(db_index=True, verbose_name='Ответ-8')
    ask_test_9 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_9 = IntegerField(db_index=True, verbose_name='Ответ-9')
    ask_test_10 = TextField(max_length=200, verbose_name='Текст вопроса')
    answers_10 = IntegerField(db_index=True, verbose_name='Ответ-10')

