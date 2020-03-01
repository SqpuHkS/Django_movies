from django.shortcuts import render
from .models import *
from django.views.generic.base import View


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies_list.html', {'movies': movies})