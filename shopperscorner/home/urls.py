from django.urls import path
from.import views
urlpatterns = [

    path('',views.index,name="homepage"),
    path("samp/", views.samp),
    path("login/",views.login,name="loginpage"),
    path("register/",views.register,name="registerpage"),
]
