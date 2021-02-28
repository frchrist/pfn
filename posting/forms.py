from django import forms
from django.forms.widgets import Select
from .models import Contact, Subscribe, Commentaire, Course, ReplayToComment



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "level", "status","img_link", "intro",  "body", 'notify_users']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class":"form-control mb-3",
        })

        self.fields['title'].label = "Titre du Cours"
        self.fields["notify_users"].widget.attrs.update({
            "class":"form-check-input",
            "id":"form-email",
        })

        self.fields['level'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['level'].label = "Le Niveau du Cours"
        self.fields['status'].widget.attrs.update({
            "class":"form-control mb-3",
        })


        self.fields['intro'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['intro'].label = "Introduction"

        self.fields['img_link'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['img_link'].label = "URL de l' Image "
        

        self.fields['body'].widget.attrs.update({
            "class":"form-control mb-3",
        })
        self.fields['body'].label = "le contenu du Cours "
class ContanctForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NewLetter(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "placeholder":"votre nom",
            'class':"btmspace-15",
        })
        self.fields['email'].widget.attrs.update({
            "placeholder":"votre email",
            'class':"btmspace-15",
        })


class CommentsForms(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['comments']

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comments"].widget.attrs.update({
            "id":"comments",
        })


class ReplayForm(forms.ModelForm):
    class Meta:
        model = ReplayToComment
        fields = ["replay_content"]


    def __init__(self):
        super().__init__()
        self.fields["replay_content"].widget.attrs.update({
            "class":"replay-form-input"
        })