from . import views
from django.urls import path

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.UserProfileListView.as_view()),
] 
