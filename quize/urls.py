
from django.urls import path
from .views import singleQuiz, listingQuizes

urlpatterns = [
    path("<slug:slug>",singleQuiz.as_view(), name="singleQuiz"),
    path("",listingQuizes.as_view(), name="listingQuizes"),

]