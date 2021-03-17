from django.urls import path
from .views import login, UserCreate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .forms import RestForm, SetPassword
from random import choices
from string import ascii_letters , digits


urlpatterns = [
    path("login/",login.as_view(), name="login"),
    path("logout/",logout.as_view(), name="logout"),
    path("register/",UserCreate.as_view(), name="register"),
    #password resting
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password/reset.html", form_class=RestForm), name="password_reset"),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(template_name="users/password/done.html"), name="password_reset_done"),
    path('password-reset-confirme/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/confirme.html", form_class=SetPassword), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="users/password/complete.html"), name="password_reset_complete"),
    #passwond Chanage
    path(f'password/change/{"".join(choices(ascii_letters+digits, k=120))}', auth_views.PasswordChangeView.as_view(template_name="users/password/changepassword.html"), name="change-pass"),
    path('password/change/done', auth_views.PasswordChangeDoneView.as_view(template_name="users/password/changepassworddone.html"), name="password_change_done"),

]
