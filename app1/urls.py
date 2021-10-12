from django.urls import path, include
from .views import helloApi, signInApi

urlpatterns = [
    path("hello/",helloApi ),
    path("sign-in/",signInApi),
]

