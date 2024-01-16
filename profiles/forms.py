from django import forms
class ProfileView(forms.Form):
    user_image=forms.FileField()
    