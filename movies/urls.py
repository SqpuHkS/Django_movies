from django.urls import path

from .views import *

urlpatterns = [
    path('', MoviesView.as_view(), name="main_page_url"),
    path('<str:url>/', MovieDetail.as_view(), name="movie_detail_url"),
]