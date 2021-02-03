from django.urls import path
from .views import login, Register, UserCreate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .forms import RestForm, SetPassword
urlpatterns = [
    path("login/",login.as_view(), name="login"),
    path("logout/",logout.as_view(), name="logout"),
    path("register/",Register.as_view(), name="register"),
    path("newuser/",csrf_exempt(UserCreate.as_view()), name="newuser"),
    #password resting
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password/reset.html", form_class=RestForm), name="password_reset"),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(template_name="users/password/done.html"), name="password_reset_done"),
    path('password-reset-confirme/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/password/confirme.html", form_class=SetPassword), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="users/password/complete.html"), name="password_reset_complete"),

]