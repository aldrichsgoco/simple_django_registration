from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#path("", views.home, name = "home"),
path("log_in/",views.log_in, name = "log_in"),
path("",views.register, name = "register"),
path("step_1/",views.step_1, name = "step_1"),
path("step_2/",views.step_2, name = "step_2"),
path("step_3/",views.step_3, name = "step_3"),
path("inside/",views.inside, name = "inside"),
path("logout/", views.log_out, name= "logout"),
]