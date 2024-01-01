from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # index means './challenges'
    path("<int:month>", views.challengesByNumber),
    path(
        "<str:month>", views.monthly_challenges, name="month-challenge"
    ),  # month_challenge=./challenges/month
]
