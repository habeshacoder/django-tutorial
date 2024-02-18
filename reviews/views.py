from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            review = Review(
                name=form.cleaned_data["user_name"],
                review=form.cleaned_data["review"],
                rate=form.cleaned_data["rate"],
            )
            review.save()
            return HttpResponseRedirect("thank_you")
        return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "We get you feedback thank you!"
        return context


class Review_List_View(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class Single_Review_View(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("kwargs:", kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get["favorite_review"]
        print("favorite_ids:", loaded_review.id, favorite_id)
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        print(' context["is_favorite"]:', context["is_favorite"])
        return context


class Add_Favorite_View(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        print("review_id:", review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

    def get(self, request):
        return HttpResponseRedirect("/reviews")
        # print('sample')
