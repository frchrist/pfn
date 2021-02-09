from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView
from django.views.generic.edit import UpdateView
from .models import Course
from .models import Level, Commentaire, ReplayToComment

from .forms import NewLetter, CommentsForms, CourseForm, ReplayForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.core.paginator import Paginator

from data.signals import object_views_signal

import threading
from django.core.mail import  EmailMessage
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.conf import settings



class email_send(threading.Thread):
    def __init__(self, email):
        super().__init__()
        self.email = email

    def run(self):
        self.email.send()
# Create your views here.
class Variables:
    def __init__(self):
        pass

    @staticmethod
    def name():
        return "Python pour les nulles"


form = NewLetter()
@method_decorator(login_required, name="dispatch")
class Profile(View):
    def get(self, request):
        context = {
            "user":request.user,
            "all": Course.objects.filter(status="Corbeille", author__username=request.user),
            "nb":Course.objects.filter(author__username=request.user),
        }
        if request.user.is_staff:
            return render(request, "adminUsers/profile.html", context=context)
        raise Http404
class HomePage(ListView):
    model= Course
    template_name = "posting/index.html"
    queryset  = Course.objects.filter(status="Publier")
    ordering = "-date"
    paginate_by = 9
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["levels"] = Level.objects.all()
        context["names"] =  Variables.name
        context["title"] = "home page"
        context["newLetterForm"] = form
        context["active"] = "active"

        return context





class CourseDetail(DetailView):
    model = Course
    template_name  ="posting/coursedetail.html"
   


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newLetterForm"] = form
        context["commentsForms"]  =CommentsForms()
        context["replayForm"]  =ReplayForm()
        #next and priviose post
        next_pk = None
        priviose_pk = None
        if self.get_object().pk < Course.objects.all().count():
            #then has next and priviose
            priviose_pk = self.get_object().pk -1
            next_pk = self.get_object().pk + 1

        elif self.get_object().pk == Course. objects.all().count():
            priviose_pk = self.get_object().pk -1
            #then has only priviose
        if self.get_object().pk == 1:
            #then only has next
            next_pk = self.get_object().pk + 1
        if next_pk != None:
            context['nexts'] =Course.objects.filter(pk=next_pk, status="Publier").first()
        if priviose_pk != None:
            context['priviouse'] =Course.objects.filter(pk=priviose_pk, status="Publier").first()


        context["levels"] = Level.objects.all()

        p = Paginator( Commentaire.objects.filter(to=self.get_object()), 3) #10 commentaire par pages
        page_n = self.request.GET.get("page")
        page_obj = p.get_page(page_n)

        context['commentaire'] = page_obj
        context['len'] = Commentaire.objects.filter(to=self.get_object()).count()
       
        display = {
            "debutant":"Débutant",
            "intermediaire":"Intermédiaire"
        }

        context['all'] = Course.objects.filter(status="Publier", level__level=self.get_object().level.level).order_by("-date")
        instance = context['object']

        object_views_signal.send(instance.__class__, instance=instance, request=self.request)

        return context


class LevelDetail(DetailView):
    model = Level
    template_name = "posting/leveldetail.html"



    def get_object(self):
        display = {
            "debutant":"Débutant",
            "intermediaire":"Intermédiaire"
        }
        value = display[self.kwargs["slug"]]
        self.level = Level.objects.get(level=value)
        return Course.objects.filter(level=self.level, status="Publier").order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(LevelDetail, self).get_context_data(**kwargs)
        context["header"]= self.level.level
        context["description"]= self.level.description
        context["newLetterForm"] = form
        context["levels"] = Level.objects.all()

        context['lTitle'] = self.kwargs["slug"]
        p = Paginator( Course.objects.filter(level=self.level, status="Publier").order_by('-date'), 9) #10 commentaire par pages
        page_n = self.request.GET.get("page")
        page_obj = p.get_page(page_n)
        context['level'] = page_obj
        return context

class NewLetterPost(View):
    def post(self, request):
        if request.is_ajax():
            form = NewLetter(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"Success":"Success"})
            else:
                return JsonResponse(dict(form.errors))
        else:
            return HttpResponse("Activer le javascript pour plus de perfommance.")



class display(View):
    def get(self, request,*args, **kwargs):
        view = CourseDetail.as_view()
        return view(request, *args, **kwargs)
    def post(self, request,*args, **kwargs):
        view = comment.as_view()
        return view(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class comment(FormView):
    form_class = CommentsForms
    template_name = "posting/coursedetail.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.to = Course.objects.get(slug=self.kwargs['slug'])
        form.save()
        froms = settings.EMAIL_HOST_USER
        message = f"{form.instance.author} à laisser un commentaire sur {form.instance.to} :  {form.instance.comments}"
        email = EmailMessage(subject="New comment", from_email=froms, body=message, to=["farechristiantanghanwaye@gmail.com"])
        email_send(email).start()
        return super(comment, self).form_valid(form)

    def get_success_url(self):
        return reverse("coursedetail", kwargs={"slug":self.kwargs['slug']})
# @method_decorator(login_required, name='dispatch')



class replay(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.user.is_authenticated:
                replayForm = ReplayForm(request.POST)
                replayForm.instance.replay_content = request.POST['replay_content']
                if replayForm.is_valid():
                    replayForm.instance.author = self.request.user
                    instanceOfcomment = Commentaire.objects.get(pk=self.kwargs['pk'])
                    replayForm.instance.to = instanceOfcomment
                    new_comment = replayForm.save()
                    comment_ser = serializers.serialize("json", [new_comment,])
                    # send email 
                    context = {'user':replayForm.instance.author, 'title':instanceOfcomment.comments, 'replay_content':replayForm.instance.replay_content, 'user_replay':self.request.user}
                    # message = render_to_string("posting/emailing.html", context)
                    # message = get_template("posting/emailing.html").render(context)
                    # message.content_subtype = "html"

                    message = f"cher(e) {instanceOfcomment.author} \n Votre commentaire '{instanceOfcomment.comments}' portant sur '{instanceOfcomment.to.title}' à été répondue par {self.request.user} \n voici le contenu :{replayForm.instance.replay_content} "

                    froms = settings.EMAIL_HOST_USER
                    to = [instanceOfcomment.author.email,]
                    email = EmailMessage(subject="Python for null : Reponse à Votre Commentaire",body=message, from_email=froms, to=to)

                    email_send(email).start()
                   
                    return JsonResponse({"response":comment_ser})
                else:
                    return HttpResponse("Svp activer le javascript de votre navigateur pour plus de perfommance ")
            else:
                return JsonResponse({"login":"Vous devez vous connecter"})
        return HttpResponse("Error")
      

        # print(replayForm.errors)

        # return HttpResponse(replayForm.as_p())
        

        


class usermixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

        if not self.has_permission():
            raise Http404

        return super(usermixin, self).dispatch(request, *args, **kwargs)

class createPost(usermixin, CreateView):
    permission_required = "posting.add_course"
    template_name = "adminUsers/create.html"
    form_class = CourseForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.image = self.request.FILES['image']
        # print(self.request.FILES)
        form.save()
        return super(createPost, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["level"] = Level.objects.all()
        return context
class CourseUpdate(usermixin, UpdateView):
    permission_required = "posting.change_course"
    model = Course
    form_class = CourseForm
    template_name = "adminUsers/create.html"


#ajaxify content views

class get_next_level_data(View):
    def get(self, request, *args, **kwargs):
        display = {
            "debutant":"Débutant",
            "intermediaire":"Intermédiaire"
        }
        value = display[self.kwargs["slug"]]
        self.level = Level.objects.get(level=value)
        initial = self.kwargs["initial"]
        data = Course.objects.filter(level=self.level)[initial:initial+3]
        data = serializers.serialize("json", data)
        return JsonResponse(data, safe=False)