from django.shortcuts import render,redirect
from django.views import View
from .models import Quize, Result, UserValidQuiz
from django.http import JsonResponse
from django.core import serializers
from time import time
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


#lister les quizes de notre applications
class listingQuizes(View):
    def get(self, request, *args, **kwargs):
        context = {
            "quizes":Quize.objects.all(),
            "valid":UserValidQuiz.objects.filter(user=request.user)
        }
        return render(request, "quize/...html", context)


@method_decorator(login_required,name="dispatch" )
class singleQuiz(View):
    def get(self, request, *args, **kwargs):
        self.quize = Quize.objects.get(slug=kwargs['slug'])
        # dico = { for quiz in Quize.objects.all()}
        context = {
            "singleQuiz":self.quize,
            "allQuiz":Quize.objects.all().exclude(),
            "allResult":Result.objects.filter(user=request.user)
          
        }
        return  render(request, "quize/single.html", context)

    def post(self, request, *args, **kwargs):
        quize =  Quize.objects.get(slug=kwargs['slug'])
        score = 0
        for questions in quize.get_qestions():
            try:
                for response in questions.get_anwsers():
                    if(response.correct and response.text == request.POST[questions.text]):
                      score += 1
            except Exception as e:
                pass
       
        #vérification si un object exitent déja à nom de l'utilisateur.
        user_result_request = Result.objects.filter(quize=quize, user=request.user)
        score = score/len(quize.get_qestions()) * 100
        
        if user_result_request.exists():
            tentative = user_result_request.last().number_of_tentative
            tentative += 1
            if score > user_result_request.last().score:
                Result.objects.update(quize=quize, user=request.user, score=score)
            Result.objects.update(quize=quize, user=request.user, number_of_tentative=tentative)
            
        else:
            result = Result.objects.create(quize=quize, user=request.user, score=score, number_of_tentative=1)
            result.save()
       	#les json à retrourner
       	#le score
       	#le nom du quize
       	#le nom de l'utilsateur
       	#l'appreciation en javascript
       	#nombre de tentatives
       	result = Result.objects.get(quize=quize, user=request.user)
       	score = score
       	min_score = result.min_score
       	quiz_name = quize.title
       	nombre_de_tentatiave = result.number_of_tentative
       	data = {"score":score, "quiz_name":quiz_name,"number_of_tentative":nombre_de_tentatiave, 'min_score':min_score}
        return JsonResponse(data)
