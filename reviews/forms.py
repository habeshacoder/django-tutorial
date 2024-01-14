from django import forms
class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=100)
    review = forms.CharField(label='Review', widget=forms.Textarea)
    rate = forms.IntegerField(label='Rate', min_value=1, max_value=5)