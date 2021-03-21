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
    
    create_at = models.DateTimeField(auto_now_add=timezone.now())
    slug = models.SlugField(blank=True, null=True, unique=True)

    def is_valid(self, username):
        for query in self.result_set.filter(user__username=username):
            if query.score >= self.duration:
                return True
        return False
   

    def get_qestions(self):
        return self.question_set.all()

    def __str__(self):
        return self.title

class Result(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   score = models.IntegerField(default=0)
   quize = models.ForeignKey(Quize, on_delete=models.CASCADE)
   appreciation = models.CharField(max_length=15, blank=True, null=True)
   min_score = models.IntegerField(default=50)
   times = models.IntegerField(blank=True, null=True)
   number_of_tentative = models.IntegerField(default=0)
   def __str__(self):
       return self.user.username


   def get_quize(self):
        return self.quize.all()

#si un resultat existe
#je verifer sonts
       




class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quize, on_delete=models.CASCADE)

    def __str__(self):
       return self.text


    def get_anwsers(self):
        return self.anwser_set.all()


class Anwser(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
       return self.text

class UserValidQuiz(models.Model):
    quize = models.ForeignKey(to=Quize, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.quize.title} - {self.is_valid}"



def createSlug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance
def createApprection(sender, instance, *args, **kwargs):
    if not instance.appreciation:
        appre = None
        if instance.score < instance.min_score:
            appre = "Mauvais"
        if instance.score >=instance.min_score:
            appre = "Bien"
        if instance.score == 100:
            appre = "Félication"

        instance.appreciation = appre
        return instance

pre_save.connect(createApprection, sender=Result)
            

pre_save.connect(createSlug, sender=Quize)
