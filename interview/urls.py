from django.urls import path
from . import views

urlpatterns = [
    # path("",views.t,name="t"),
    # path("rrr",views.rrr,name="rrr"),
    path("",views.home,name="home"),
    path("test/",views.test,name="test"),
    path("evaluate/",views.evaluate,name="evaluate"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact")
]