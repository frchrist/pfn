from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"inputbox",
        "placeholder":"Utilisateur"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"inputbox",
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

class RestForm(PasswordResetForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "class":"inputbox",
            "placeholder":"Email"
        })

class SetPassword(SetPasswordForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({
             "class":"inputbox",
            "placeholder":"Nouveau mot de passe"
        })
        self.fields["new_password2"].widget.attrs.update({
             "class":"inputbox",
            "placeholder":"Confirmer le  mot de passe"
        })
        

class RegisterForm(UserCreationForm):
    error_css_class = "error"
    error_class = "error"
    class Meta:
        model = User
        fields = ["first_name", "username", "email","password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class":"inputbox",
             "placeholder":"Prenom "
        })
        self.fields["username"].widget.attrs.update({
            "class":"inputbox",
            "placeholder":"Utilisateur"
        })
        self.fields["email"].widget.attrs.update({
            "class":"inputbox",
             "placeholder":"Email"
        })
        self.fields["password1"].widget.attrs.update({
            "class":"inputbox",
             "placeholder":"Mot de passe"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"inputbox",
            "placeholder":"Comfirmer le mot de passe"
        })

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Adresse électronique déja prise")

        return self.cleaned_data['email'] 


