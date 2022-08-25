from django.urls import path
from.import views
urlpatterns = [

    path('',views.index),
    path("samp/", views.samp),
    path("login/",views.login),
    path("register/",views.register),
    path("login/logincheck/",views.logincheck),
    path("register/registercheck/",views.registercheck),
]
