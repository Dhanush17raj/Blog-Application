from unicodedata import name
from django.urls import path
from . import views
 ###local:8000/studyplanner/home
urlpatterns = [
     path('about', views.about, name = 'studyplanner-about'),
     path('home', views.home, name = 'studyplanner-home')
    # path('<day>', views.weekly_timetable, name = "fggh")
 ]