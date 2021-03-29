from django.urls import path, include
from .views import ContactUs, HomePage, CourseDetail, createPost, display, CourseUpdate, replay


urlpatterns = [
    path("",HomePage.as_view(), name="homepage"),
    path("contact-us/", ContactUs.as_view(), name="contact-us"),
    path('python-course/<slug:slug>', display.as_view(), name="coursedetail"),
     path('python-course/<slug:slug>/@admin/edit/course', CourseUpdate.as_view(), name="update"),
    path("@admin/add-new/course",createPost.as_view(), name="create" ),
    path("replay/",replay.as_view(), name="replay"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]