from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthsDec = {
    "jan": "jan",
    "feb": "feb",
    "mar": "mar",
    "apr": "april",
    "may": None,
}


# Create your views here.
def index(request):
    months = list(monthsDec.keys())
    return render(request, "challenges/index.html", {"months": months})


def challengesByNumber(request, month):
    months = list(monthsDec.keys())

    redirect_month = months[month - 1]
    if month > len(months):
        return HttpResponseNotFound("page not available")
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# diplay a month challenge
def monthly_challenges(request, month):
    try:
        challenge_text = monthsDec[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "challenge": month},
        )

    except:
        raise Http404()
