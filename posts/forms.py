from users.models import Post
from django import forms

class PostCreationForm(forms.Form):
    name = forms.CharField(max_length=20)
    occupation = forms.CharField(widget=forms.Textarea(), max_length=10)

