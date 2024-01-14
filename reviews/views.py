from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView


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


class Single_Review_View(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("kwargs:", kwargs)
        selected_review_id = kwargs["id"]
        review = Review.objects.get(pk=selected_review_id)
        context["review"] = review
        return context
