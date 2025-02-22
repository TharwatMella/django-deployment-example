from django.urls import path
from basic_app import views

app_name='start'

urlpatterns = [
    path("relative",views.relative,name="relative"),
    path("other",views.other,name="other"),
    path("index",views.index,name="index"),
    path("nameForm",views.name_Form,name="nameForm")
]