from django.urls import path
from .views import by_rubric, index, profile 
from .views import other_page, profile, user_activate, detail, books_page

from .views import BBLoginView, BBLogoutView
from .views import ChangeUserInfoView, DeleteUserView
from .views import RegisterUserView, RegisterUserDone
from .views import BBPasswordReset, BBPasswordResetDone, BBPasswordResetConfirm
from .views import BBPasswordResetComplete, BBPasswordChangeView
from .views import profile_bb_add, profile_bb_change, profile_bb_delete, profile_bb_detail

app_name = 'main'
urlpatterns = [
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('other/books/', books_page, name='books'),
    path('', index, name='index'),

    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterUserDone.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),

    path('accounts/profile/delete', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),

    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password/password_reset/', BBPasswordReset.as_view(), name='password_reset'),
    path('accounts/password/password_reset_done/', BBPasswordResetDone.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', BBPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('accounts/reset/complete/', BBPasswordResetComplete.as_view(), name='password_reset_complete'),
]