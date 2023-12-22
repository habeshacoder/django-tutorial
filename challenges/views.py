from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def january(request):
    return HttpResponse("working")


def monthly_challenges(resquest, month):
    challenge_text = None

    if month == "february":
        challenge_text = "welcome to february"
    elif month == "jan":
        challenge_text = "welcome to january"
    elif month == "ju":
        challenge_text = "welcome to ju"
    else:
        return HttpResponseNotFound("no page is availble for your request")
    return HttpResponse(challenge_text)
