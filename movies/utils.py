from django.shortcuts import render, redirect, get_object_or_404
from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, url):
        obj = get_object_or_404(self.model, url__iexact=url)
        return render(request, self.template, context={self.model.__name__.lower():obj})