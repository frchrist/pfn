from django.urls import path, include
from .views import HomePage, CourseDetail, LevelDetail, NewLetterPost, createPost, display, CourseUpdate, Profile
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("",HomePage.as_view(), name="homepage"),
    path('python-course/<slug:slug>', display.as_view(), name="coursedetail"),
     path('python-course/<slug:slug>/edit', CourseUpdate.as_view(), name="update"),
    path('python-course-level/<slug:slug>', LevelDetail.as_view(), name="niveaudetail"),
    path("newletters", csrf_exempt(NewLetterPost.as_view()), name="newletter"),
    path("make-new-course",createPost.as_view(), name="create" ),
     path("accounts/profile",Profile.as_view(), name="profile" ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]