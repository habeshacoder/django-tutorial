from . import views
from django.urls import path

app_name = "reviews"
urlpatterns = [
    path("", views.ReviewView.as_view(), name="add_review"),
    path("thank_you", views.ThankYouView.as_view(), name="thank_page"),
    path("reviews", views.Review_List_View.as_view(), name="reviews_list"),
    path("reviews/<int:pk>", views.Single_Review_View.as_view(), name="review_detail"),
    path("reviews/favorite", views.Add_Favorite_View.as_view(), name="add_favorite"),
]
