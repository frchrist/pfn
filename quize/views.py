from django.shortcuts import render,redirect
from django.views import View
from .models import Quize, Result


# Create your views here.


#lister les quizes de notre applications
class listingQuizes(View):
    def get(self, request, *args, **kwargs):
        context = {
            "quizez":Quize.objects.all()
        }
        return render(request, "quize/...html", context)


class singleQuiz(View):
    def get(self, request, *args, **kwargs):
        context = {
            "singleQuiz":Quize.objects.get(slug=kwargs['slug'])
        }
        return  render(request, "quiz/single.html", context)

    def post(self, request, *args, **kwargs):
        close = time.time() - float(request.POST['time'])
        name = request.POST['q_name']
        quiz = Quiz.objects.filter(name=name).first()
        if close > quiz.durre*60:
           return render(request, "quiz/index.html")

        #  print(quiz)
        score = 0
        for questions in quiz.get_qestions():
            try:
                for response in questions.get_responses():
                    if(response.correct and response.text == request.POST[questions.text]):
                      score += 1
            except Exception as e:
                print(e)

        result = Result.objects.create(q_name=quiz, user=request.user, score=score/4 * 100)
        result.save()
        return redirect("result")
