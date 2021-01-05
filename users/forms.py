from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input100",
        "name":"username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"input100",
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
            "class":"input100"
        })
        self.fields["username"].widget.attrs.update({
            "class":"input100"
        })
        self.fields["email"].widget.attrs.update({
            "class":"input100"
        })
        self.fields["password1"].widget.attrs.update({
            "class":"input100"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"input100"
        })
