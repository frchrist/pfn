from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, RegisterForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from django.views.generic import UpdateView
from django.contrib.auth.models import User

from posting.models import Course
# Create your views here.




class login(LoginView):
    template_name = "up-posting/auth/login.html"
    authentication_form = LoginForm


class UserCreate(View):
    def get(self, request):
        context = {
            "form":RegisterForm()
        }

        return render(request, "up-posting/auth/register.html", context=context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="students")
            group.user_set.add(user)
            messages.success(request, "Votre compte à bien été créer connecter vous")
            return redirect("login")
        else:
             context = {
            "form":form
        }

        return render(request, "up-posting/auth/register.html", context=context)


@method_decorator(login_required, name="dispatch")
class Profile(UpdateView):
    model = User
    fields = ["username", "email"]
    template_name ="up-posting/auth/profile.html"

    def get_object(self, *args) :
        queryset = User.objects.filter(username=self.request.user)
        return super().get_object(queryset=queryset)
    def get_success_url(self) -> str:
        return reverse("profile", kwargs={"pk":self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(self.request.user.is_staff):
            context["recycleBin"] =  Course.objects.filter(status="Corbeille", author__username=self.request.user)
        return context



class logout(LogoutView):
    pass