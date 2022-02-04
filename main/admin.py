# Тут прописываются все функции админ.сайта
from django.contrib import admin
import datetime
from .models import AdvUser
from .models import SubRubric, SuperRubric, Bb
from .forms import SubRubricForm


# модель пользователей с параметрами отобажения
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    fields = ('email', ('first_name', 'last_name'), ('is_active', 'is_activated'),
              ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(AdvUser, AdvUserAdmin)


# код классов редактора SuperRubricAdmin и встроенного редактора Sub_Rubric_inline.
class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(SuperRubric, SuperRubricAdmin)


# Работа с объявлениями
class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'author', 'created_at')
    fields = (('rubric', 'author'), 'title', 'image', 'is_active')


admin.site.register(Bb, BbAdmin)
