from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from profiles.forms import ProfileView
from profiles.models import UserProfile
from django.views.generic import CreateView, ListView

# Create your views here.


class CreateProfileView(CreateView):
    model = UserProfile
    fields = ["user_image"]
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileView()
#         return render(
#             request,
#             "profiles/create_profile.html",
#             {
#                 "form": form,
#             },
#         )

#     def post(self, request):
#         image = ProfileView(request.POST, request.FILES)
#         if image.is_valid:
#             imagefile = UserProfile(user_image=request.FILES["user_image"])
#             imagefile.save()
#         return HttpResponseRedirect("/profiles")
