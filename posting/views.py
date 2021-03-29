from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView
from django.views.generic.edit import UpdateView
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
from django.core.mail import  EmailMessage
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.conf import settings
from .models import Course
from .models import Level, Commentaire, ReplayToComment
from .forms import NewLetter, CommentsForms, CourseForm, ReplayForm, ContactForm
import threading
from data.signals import object_views_signal
from quize.models import Quize


class sendEmail(threading.Thread):
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


class HomePage(ListView):
    model= Course
    template_name = "up-posting/pages/home.html"
    queryset  = Course.objects.filter(status="Publier").order_by("-date")
    ordering = "-date"
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["names"] =  Variables.name
        context["title"] = "Bienvenue sur PythonForNull"
        context['leated_course_posted'] = self.queryset[:6]
        context["quizes"] = Quize.objects.all()
        context['tutos'] = self.queryset.filter(type="Tutoriels").order_by("-date")
        return context




class CourseDetail(DetailView):
    model = Course
    template_name  ="up-posting/pages/post-detail.html"
    context_object_name = "onecourse"


    def getNextItem(self, *args, **kwargs):
        currentObject = self.get_object()
        Next = Course.objects.filter(pk__gt=currentObject.pk).first()
        return Next

    def getPriviouseItem(self, *args, **kwargs):
        currentObject = self.get_object()
        prev = Course.objects.filter(pk__lt=currentObject.pk).last()
        return prev


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = context["onecourse"]
        object_views_signal.send(instance.__class__, instance=instance, request=self.request)
        
        lists = {
                "nexts": self.getNextItem(), 
                "prev":self.getPriviouseItem(),
                "commentsForms":CommentsForms(),
                "ReplayForm":ReplayForm(),
                "all":Course.objects.filter(status="Publier", level__level=self.get_object().level.level).order_by("-date"), 

                }
        for key,value in lists.items():
            context[key] = value
        

        return context


class display(View):
    def get(self, request,*args, **kwargs):
        view = CourseDetail.as_view()
        return view(request, *args, **kwargs)
    def post(self, request,*args, **kwargs):

        if self.request.is_ajax():
            print(kwargs)
            forms = CommentsForms(self.request.POST)
            if forms.is_valid():
                course = Course.objects.get(slug=self.kwargs['slug'])
                forms.instance.author = request.user
                forms.instance.to = course
                forms.save()
                strings = render_to_string("up-posting/render_.html", {"onecourse":course})
                return JsonResponse({"data":strings})
                # return JsonResponse(last_insert, safe=False)
            else:
                return HttpResponse(forms.errors)
        else:
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
        forms  = ReplayForm(self.request.POST)
        if forms.is_valid():
            forms.instance.author = self.request.user
            #input de type hidden qui contiendra l'id_pk du commentaire ainsi repondu
            instanceOfcomment = Commentaire.objects.filter(id_pk=self.request.POST['hidden']).first()
            forms.instance.to = instanceOfcomment
            ##############################""""
            # DEBUG
            forms.save()
            #######################################
             # send email 
            full_path = f"{request.get_host()}/python-course/{instanceOfcomment.to.slug}#{instanceOfcomment.id_pk}"
            context = {'replay_maker':forms.instance.author, 'replay_content':forms.instance.replay_content,"path":full_path, 'commente_maker':instanceOfcomment.author}
            message = render_to_string("up-posting/emails/replays.html", context)
            # message = get_template("up-posting/emails/replays.html").render(context)
            # message.content_subtype = "html"

            # message = f"cher(e) {instanceOfcomment.author} \n Votre commentaire '{instanceOfcomment.comments}' portant sur '{instanceOfcomment.to.title}' à été répondue par {self.request.user} \n voici le contenu :{replayForm.instance.replay_content} "
            froms = settings.EMAIL_HOST_USER
            to = [instanceOfcomment.author.email,]
            subject="Python for null : Réponse à Votre Commentaire"
            email = EmailMessage(subject=subject,body=message,from_email=froms, to=to)
            email.content_subtype = "html"
            

            sendEmail(email).start()
            if self.request.is_ajax():
                strings = render_to_string("up-posting/render_.html", {"onecourse":instanceOfcomment.to})
                return JsonResponse({"data":strings})

            else:
               return HttpResponse("Svp activer le javascript de votre navigateur pour plus de performance ")
            
       

class usermixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

        if not self.has_permission():
            raise Http404

        return super(usermixin, self).dispatch(request, *args, **kwargs)

class createPost(usermixin, CreateView):
    permission_required = "posting.add_course"
    template_name = "up-posting/pages/upload-course.html"
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
    template_name = "up-posting/pages/upload-course.html"

#la page de contact

class ContactUs(View):
    def get(self, request, *args,**kwargs):
        form = ContactForm()
        return render(request, "up-posting/pages/contact.html", {"form":form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "votre message à été bien reçu")
            return redirect("homepage")
        else:
            messages.warning(request, "le formulaire que vous nous avez envoyer est incorrect")
            return redirect("contact-us")