from django.contrib import admin
from django.urls import path,include
from .views import movieview,NotesVies,ActorVies,SongsVies,ImageView
urlpatterns = [

    #direct show(get)
    path('songs',SongsVies.as_view()),
    path('notes',NotesVies.as_view()),

    #inside actor added(get,post)
    path('actor',ActorVies.as_view()),
    path('actor/<pk>/',ActorVies.as_view()),
    
    #inside movie added(get,post)
    path('movie',movieview.as_view()),
    path('movie/<pk>/',movieview.as_view()),
    path('movie/<pk>/note',NotesVies.as_view()),
    path('movie/<pk>/song',SongsVies.as_view()),
    path('movie/<pk>/imgs',ImageView.as_view())
]
