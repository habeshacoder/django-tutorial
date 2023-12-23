from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month>", views.challengesByNumber),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
]

