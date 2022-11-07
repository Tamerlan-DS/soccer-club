from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',MainView,name="main-page"),
    path('matches/',MatchesView,name="matches"),
    path('players/',PlayersView,name='players'),
    path('about/',AboutUsView,name='about'),
    path('contacts/',ContactsView,name='contacts'),
]
