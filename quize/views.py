from django.shortcuts import render,redirect
from django.views import View
from .models import Quize, Result, UserValidQuiz
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from time import time
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils import timezone
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
        user_result_request = Result.objects.filter(quize=self.quize, user=request.user)
        if(user_result_request.exists()):
            x = user_result_request.first().last_do - timezone.now()
            if(x.days <= 0):
                messages.warning(request, "Ce quize n'est plus disponible pour vous pour cette journé")
                return redirect("homepage")
        # dico = { for quiz in Quize.objects.all()}
        context = {
            "singleQuiz":self.quize,
            "quizes":Quize.objects.all().exclude(),
            "allResult":Result.objects.filter(user=request.user)
          
        }
        return  render(request, "up-posting/quize/index.html", context)

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
        #####################debug#####################""
        # return JsonResponse({"resultat":False})
        ###############################################
        #vérification si un object exitent déja à nom de l'utilisateur.
        user_result_request = Result.objects.filter(quize=quize, user=request.user)
        score = score/len(quize.get_qestions()) * 100
        
        if user_result_request.exists():
            #intervalue d'une journé
            x = user_result_request.first().last_do - timezone.now()
            if(x.days <= 0):
                messages.success(request, "il faut un délai d'une journé avant de repouvoir faire ce quize")
                return JsonResponse({"errors":"/"})
            
            tentative = user_result_request.last().number_of_tentative
            tentative += 1
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
       	result = Result.objects.filter(quize=quize, user=request.user).first()
       	context = {
               "resultat":result
           }
        string = render_to_string("up-posting/quize/result.html", context)
        print(string)
        return JsonResponse({"result":string})
        
       	# data = {"score":score, "quiz_name":quiz_name,"number_of_tentative":nombre_de_tentatiave, 'min_score':min_score}
        # return JsonResponse(data)
