from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import reverse, redirect
from django.db.models.signals import pre_save
from ckeditor.fields  import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ModelUtile:
    def __init__(self):
        pass

    @staticmethod
    def slug(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.title)


course_level = [("Débutant", "Débutant"), ("Intermédiaire","Intermédiaire")]
course_status = [("Publier", "publier"), ("Corbeille","corbeille")]
class Level(models.Model):
    level = models.CharField(choices=course_level, max_length=13)
    description = models.TextField(default="ceci est un niveau")

    def __str__(self):
        return self.level

class Course(models.Model):
    title = models.CharField(max_length=225)
    level = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=course_status, max_length=13, default="publier")
    slug = models.SlugField(blank=True, unique=True)
    body = RichTextUploadingField(verbose_name='content')
    intro = RichTextUploadingField(blank=1, null=1, config_name="extrait")
    img_link = models.URLField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('coursedetail', kwargs={"slug":self.slug})




    def __str__(self):
        return self.title

    

class Base_info(models.Model):
    name  = models.CharField(max_length=155)
    email = models.EmailField()
    class Meta:
        abstract = True
class Contact(Base_info):
    message = models.TextField()


class Subscribe(Base_info):
    pass

class Commentaire(models.Model):
    comments = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    at = models.DateTimeField(auto_now_add=True)
    to = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return "commentaire de "+author

pre_save.connect(ModelUtile.slug, Course)

