from django import forms
from django.db import models
from django.forms import fields, inlineformset_factory, widgets, inlineformset_factory
from .models import AdvUser

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .apps import user_registered
from .models import SubRubric, SuperRubric
from .models import Bb, TestBody


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(forms.ModelForm):  # Form for registration user
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (Повторно)', widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль для проверки')

    # выполняем валидацию пароля
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    # проверяем, совпадают ли оба введенных пароля
    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    # save users in data base
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


# Форма для Под- и Над- рубрик
class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(queryset=SuperRubric.objects.all(), empty_label=None, label='Надрубрика',
                                          required=True)  # обязательное заполнение поля Надрубрик

    class Meta():
        model = SubRubric
        fields = '__all__'


# Форма строки поиска по искомому слову
class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='Искать...')


# форма для добавления и редактирования теста пользователя
class BbForm(forms.ModelForm):
    class Meta():
        model = Bb
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


class TestBodyForm(forms.ModelForm):
    class Meta():
        model = TestBody
        fields = '__all__'


AIFormSet = inlineformset_factory(Bb, TestBody, fields='__all__', extra=1)

class Form_for_examination(forms.Form):
    answer_form_1 = forms.CharField(label='Ответ', max_length=100)
    answer_form_2 = forms.CharField(label='Ответ', max_length=100)
    answer_form_3 = forms.CharField(label='Ответ', max_length=100)
    answer_form_4 = forms.CharField(label='Ответ', max_length=100)
    answer_form_5 = forms.CharField(label='Ответ', max_length=100)
    answer_form_6 = forms.CharField(label='Ответ', max_length=100)
    answer_form_7 = forms.CharField(label='Ответ', max_length=100)
    answer_form_8 = forms.CharField(label='Ответ', max_length=100)
    answer_form_9 = forms.CharField(label='Ответ', max_length=100)
    answer_form_10 = forms.CharField(label='Ответ', max_length=100)
