from django.contrib import admin
from .models import Actor, Category, Genre, MovieShots, Movie, Reviews, Rating, RatingStar

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)

