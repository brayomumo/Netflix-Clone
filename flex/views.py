from django.shortcuts import render
import requests
from .models import Movie

# Create your views here.
def index(request):
    
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=53484a41a25b39d53b7b490c5feaf4e9'
    r = requests.get(url.format()).json()
    movie_list = r['results']
    # print(movie_list)
    percent = 100
    images = []
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster_path = movie_item.get('poster_path')
        # print(poster_path)
        rating = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count'),
        age = movie_item.get('genre_ids[3]')
        percent = percent-3
        images.append(poster_path)
        if poster_path:
            movie_object = Movie(id,title,overview,poster_path,rating,vote_count,age,percent) 
            movie_results.append(movie_object)
        # print(movie_results.image)
        # print(movie_results)

    
    return render(request, "index.html", {"all": movie_results, "images": images})




def homepage(request):
    return render(request,'homepge.html')

