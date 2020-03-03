from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from .utils import *


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'main_page.html', {'movies': movies})

class MovieDetail(ObjectDetailMixin, View):
    model = Movie
    template = 'movie_detail.html'