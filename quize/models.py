from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.


class Quize(models.Model):
    title  = models.CharField(max_length=225)
    topic =  models.CharField(max_length=225)
    duration = models.IntegerField(default=0)
    min_score = models.IntegerField(default=50)
    create_at = models.DateTimeField(auto_now_add=timezone.now())
    slug = models.SlugField(blank=True, null=True, unique=True)
   

    def get_qestions(self):
        return self.question_set.all()

class Result(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   score = models.IntegerField(default=0)
   quize = models.OneToOneField(Quize, on_delete=models.CASCADE)



   def get_quize(self):
        return self.quize.all()




class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quize, on_delete=models.CASCADE)

    def get_anwsers(self):
        return self.anwser_set.all()


class Anwser(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)







def createSlug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance


pre_save.connect(Quize, createSlug)
