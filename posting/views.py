from django.shortcuts import render, reverse, redirect
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView
from django.views.generic.edit import UpdateView
from .models import Course
from .models import Level, Commentaire

from .forms import NewLetter, CommentsForms, CourseForm
from django.http import JsonResponse, HttpResponse

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Variables:
    def __init__(self):
        pass

    @staticmethod
    def name():
        return "Python pour les null"

form = NewLetter()
class HomePage(ListView):
    model= Course
    template_name = "posting/index.html"
    queryset  = Course.objects.filter(status="publier")
    ordering = "-date"
    paginate_by = 1
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["levels"] = Level.objects.all()
        context["names"] =  Variables.name
        context["title"] = "home page"
        context["newLetterForm"] = form
        return context





class CourseDetail(DetailView):
    model = Course
    template_name  ="posting/coursedetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newLetterForm"] = form
        context["commentsForms"]  =CommentsForms()
        context["levels"] = Level.objects.all()
        context['commentaire'] = Commentaire.objects.filter(to=self.get_object())

        return context


class LevelDetail(DetailView):
    model = Level
    template_name = "posting/leveldetail.html"


    def get_object(self):
        self.level = Level.objects.get(level=self.kwargs["slug"])
        return Course.objects.filter(level=self.level)

    def get_context_data(self, **kwargs):
        context = super(LevelDetail, self).get_context_data(**kwargs)
        context["header"]= self.level.level
        context["description"]= self.level.description
        context["newLetterForm"] = form
        context["levels"] = Level.objects.all()
        context['lTitle'] = self.kwargs["slug"]
       
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
            return HttpResponse("Activer le javascript pour plus de perfomment de  notre site .")



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
        return super(comment, self).form_valid(form)
        # return render_to_response(reverse("coursedetail", kwargs=))

    def get_success_url(self):
        return reverse("coursedetail", kwargs={"slug":self.kwargs['slug']})


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