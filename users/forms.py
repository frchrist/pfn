from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Utilisateur"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Mot de passe"
    }))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(**kwargs)
    #     self.fields["password"].widget.attrs.update({
    #         "name":"pass",
    #     })

    error_messages = {
        "invalid_login":_("le nom utilisateur ou le mot de passe incorrect")
    }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "username", "email","password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class":"form-control",
             "placeholder":"Prenom "
        })
        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Utilisateur"
        })
        self.fields["email"].widget.attrs.update({
            "class":"form-control",
             "placeholder":"Email"
        })
        self.fields["password1"].widget.attrs.update({
            "class":"form-control",
             "placeholder":"Mot de passe"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"Comfirmer le mot de passe"
        })
