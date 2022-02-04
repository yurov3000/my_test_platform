from .models import AdvUser, SubRubric, Bb, TestBody
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.http import HttpResponse, Http404

from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ChangeUserInfoForm, BbForm, AIFormSet, TestBodyForm

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView
from .forms import RegisterUserForm

from django.core.signing import BadSignature
from .utilites import signer

from django.views.generic.edit import DeleteView
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView

from django.core.paginator import Paginator
from django.db.models import Q
from .forms import SearchForm, Form_for_examination
from django.forms import formset_factory
import requests
from requests.structures import CaseInsensitiveDict


# главная страница
def index(request):
    bbs = Bb.objects.filter()

    # фильтрация записей по введенному слову
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        bbs = bbs.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})  # передаем полученное ранее искомое слово

    paginator = Paginator(bbs, 2)  # настраиваем пагинатор
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'page': page, 'bbs': page.object_list, 'form': form}  # создаем контекст
    return render(request, 'main/index.html', context=context)


# вспомогательные страницы
def other_page(request, page):  # какой-либо индефикатор страницы передается в контроллер, и уже потом выдается страница
    try:
        template = get_template('main/' + page + '.html')  # передаем имя шаблона страницы
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


# вспомогательные страницы с доп материалом
def books_page(request):
    template_name = 'main/books.html'
    context = {'template_name': template_name}
    return render(request, 'main/books.html', context=context)


class BBLoginView(LoginView):  # регистрация/вход
    template_name = 'main/login.html'


class BBLogoutView(LogoutView, LoginRequiredMixin):  # страница выхода
    template_name = 'main/logout.html'


@login_required
def profile(request):  # страница профиля пользователя + вывод списка тестов пользователя
    bbs = Bb.objects.filter(author=request.user.pk)
    context = {'bbs': bbs}
    return render(request, 'main/profile.html', context)


@login_required
def profile_bb_detail(request, pk):  # страница тестов зарег. пользователя
    bb = get_object_or_404(Bb, pk=pk)
    context = {'bb': bb}
    return render(request, 'main/profile_bb_detail.html', context)


@login_required
def profile_bb_add(request):  # Контроллер для публикования теста  из редактора
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES)
        if form.is_valid():  # Проверяем форму на правильность введенных данных
            bb = form.save()  # Сохраняем тест
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Тест добавлен.')
                return redirect('main:profile')  # перенаправляем на страницу профиля
    else:
        form = BbForm(initial={'author': request.user.pk})  # возвращаем к исходной форме на странице пользователя
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_add.html', context)  # рендерим страницу


@login_required
def profile_bb_change(request, pk):  # Контроллер для редактирования теста из редактора
    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES, instance=bb)
        if form.is_valid():  # Проверяем форму на правильность введенных данных
            bb = form.save()  # Сохраняем тест
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Тест изменен.')
                return redirect('main:profile')  # перенаправляем на страницу профиля
    else:
        form = BbForm(instance=bb)
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_bb_change.html', context)


@login_required
def profile_bb_delete(request, pk):  # Контроллер для удаления теста
    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        bb.delete()
        messages.add_message(request, messages.SUCCESS, 'Тест удален.')
        return redirect('main:profile')  # перенаправляем на страницу профиля
    else:
        context = {'bb': bb}
        return render(request, 'main/profile_bb_delete.html', context)


# Страница изменения информации о пользователе
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя успешно изменены'

    def setup(self, request, *args, **kwargs):  # ключ текущего пользователя
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):  # Извлечение исправляемой записи
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


# Страница изменения пароля
class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль успешно изменен'


# Формирование формы для сброса пароля.
class BBPasswordReset(PasswordResetView):
    template_name = 'main/password_reset_form.html'
    subject_template_name = 'email/reset_password_subject.txt'
    email_template_name = 'email/reset_password_body.txt'
    success_url = reverse_lazy('main:password_reset_done')


# страница уведомления об успешной отправке эл.письма для сброса пароля
class BBPasswordResetDone(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'
    success_message = 'Письмо тправлено...'


# Механизм сброса пароля.
class BBPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'main/password_reset_confirm.html'
    post_reset_login = True
    success_url = reverse_lazy('main:password_reset_complete')


# сообщение об успешном сброве пароля
class BBPasswordResetComplete(PasswordResetCompleteView):
    template_name = 'main/password_reset_complete.html'
    success_message = 'Пароль успешно изменен'


# Контроллер-класс, регистрирующий пользователя
class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterUserDone(TemplateView):
    template_name = 'main/register_user_done.html'


# Веб-страницы активации пользователя
def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


# Страница удаления пользователя
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    # сохранили ключ текущего пользователя
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    # Перед удалением текущего пользователя необходимо выполнить выход
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    # отыскали по этому ключу пользователя, подлежащего удалению
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


# Рубрики
def by_rubric(request, pk):
    rubric = get_object_or_404(SubRubric, pk=pk)
    bbs = Bb.objects.filter(is_active=True, rubric=pk)  # фильтр записей помеченных для вывода "is_active"

    # фильтрация записей по введенному слову
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        bbs = bbs.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})  # передаем полученное ранее искомое слово

    paginator = Paginator(bbs, 2)  # настраиваем пагинатор
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'rubric': rubric, 'page': page, 'bbs': page.object_list, 'form': form}  # создаем контекст
    return render(request, 'main/by_rubric.html', context=context)  # рендерим страницу


# Сведения о быбранном тесте
def detail(request, rubric_pk, pk):
    bb = get_object_or_404(Bb, pk=pk)
    test = get_object_or_404(TestBody, pk=pk)
    
    if request.method == 'POST':
        answer_form = Form_for_examination(request.POST)
        if answer_form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Ответы отправлены на проверку')
            return redirect('main:profile')
             
    else:
        answer_form = Form_for_examination() 
                                                                               
    context = {'bb': bb, 'test': test, 'answer_form': answer_form}
    return render(request, 'main/detail.html', context)

""" 
def check_test(request, headers=CaseInsensitiveDict()):
    url = "http://127.0.0.1:8000/"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "key1=value1&key2=value2"

    resp = request.post(url, headers=headers, data=data)
    print(resp.status_code)

    return resp """

















