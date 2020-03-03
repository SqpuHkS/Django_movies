from django import forms
from .models import *


class MoviePost(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = [""]

    def clean_slug(self):
        new_slug = self.cleaned_data['url'].lower()
        return new_slug