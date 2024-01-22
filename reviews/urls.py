from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_you", views.ThankYouView.as_view()),
    path("reviews", views.Review_List_View.as_view()),
    path("reviews/<int:id>", views.Single_Review_View.as_view()),
    path("reviews/favorite", views.Add_Favorite_View.as_view(),name='add_favorite'),
]
