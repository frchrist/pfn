from django.urls import path, include
from .views import HomePage, CourseDetail, LevelDetail, NewLetterPost, createPost, display, CourseUpdate
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("",HomePage.as_view(), name="homepage"),
    path('course/<slug:slug>', display.as_view(), name="coursedetail"),
     path('course/<slug:slug>/edit', CourseUpdate.as_view(), name="update"),
    path('niveau/<slug:slug>', LevelDetail.as_view(), name="niveaudetail"),
    path("newletter", csrf_exempt(NewLetterPost.as_view()), name="newletter"),
    path("create-cours",createPost.as_view(), name="create" ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]