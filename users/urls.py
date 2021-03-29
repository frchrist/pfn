from django.urls import path
from .views import login, UserCreate, logout, Profile
from django.contrib.auth import views as auth_views
from .forms import RestForm, SetPassword
from random import choices
from string import ascii_letters , digits


urlpatterns = [
    path("profile/<int:pk>",Profile.as_view(), name="profile" ),
    path("login/",login.as_view(), name="login"),
    path("logout/",logout.as_view(), name="logout"),
    path("register/",UserCreate.as_view(), name="register"),
    #password resting
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="up-posting/auth/password-reset.html", form_class=RestForm), name="password_reset"),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(template_name="up-posting/auth/password-reset-done.html"), name="password_reset_done"),
    path('password-reset-confirme/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="up-posting/auth/password-reset-confirme.html", form_class=SetPassword), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="up-posting/auth/password-reset-complete.html"), name="password_reset_complete"),
    #passwond Change
    path(f'password/change/{"".join(choices(ascii_letters+digits, k=120))}', auth_views.PasswordChangeView.as_view(template_name="up-posting/auth/change-password.html"), name="change-pass"),
    path('password/change/done', auth_views.PasswordChangeDoneView.as_view(template_name="up-posting/auth/password-change-done.html"), name="password_change_done"),

]
