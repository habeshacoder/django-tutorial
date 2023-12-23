from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthsDec = {
    "jan": "jan",
    "feb": "feb",
    "mar": "mar",
    "apr": "april",
    "may": "may",
}


# Create your views here.
def index(request):
    listItems = ""
    months = list(monthsDec.keys())
    for month in months:
        capitilized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        listItems += f'<li><a href="{month_path}">{capitilized_month}</a></li>'

    response_data = f"<ul>{listItems}</ul>"
    return HttpResponse(response_data)


def challengesByNumber(request, month):
    months = list(monthsDec.keys())

    redirect_month = months[month - 1]
    if month > len(months):
        return HttpResponseNotFound("page not available")
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(resquest, month):
    try:
        challenge_text = monthsDec[month]
        return HttpResponse(challenge_text)

    except:
        HttpResponseNotFound("page not found")
