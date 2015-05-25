from django.shortcuts import render
from django.views.generic import View
from .models import Movie


class IndexView(View):

    def get(self, request):
        all_movies = Movie.objects.all()

        return render(request, "index_view.html", {"movies": all_movies})
