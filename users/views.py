from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, RegisterForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from django.contrib.auth.models import Group
# Create your views here.



class login(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm


class Register(View):
    def get(self, request):
        context = {
            "form":RegisterForm()
        }

        return render(request, "users/register.html", context=context)


class UserCreate(View):
    def post(self, request):
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='students')
                group.user_set.add(user)

                return JsonResponse({"success":"success"})
            else:
                return JsonResponse(dict(form.errors))
        else:
            return JsonResponse({"error":"please active javascript"})


class logout(LogoutView):
    pass