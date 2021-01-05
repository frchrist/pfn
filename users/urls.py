from django.urls import path
from .views import login, Register, UserCreate, logout
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("login/",login.as_view(), name="login"),
    path("logout/",logout.as_view(), name="logout"),
    path("register/",Register.as_view(), name="register"),
    path("newuser/",csrf_exempt(UserCreate.as_view()), name="newuser"),
]