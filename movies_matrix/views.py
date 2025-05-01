from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import Movie
from django.db.models import Q

def login_redirect(request):
    return redirect('login')  # to login page

def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): #if details are valid
            form.save() #save user
            return redirect('login') #sends to login after create account
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_account.html', {'form': form})


def home(request):
    return render(request, 'homepage.html') #to homepage


def search_results(request):
    query = request.GET.get('search')
    if query:
        results = Movie.objects.filter(
            Q(movie_title__icontains=query) |
            Q(casting__actor_actor__actor_first_name__icontains=query) |
            Q(casting__actor_actor__actor_last_name__icontains=query) |
            Q(genremovieassignment__genre_genre__genre_name__icontains=query) |
            Q(moviedirectorassignment__director_director__director_first_name__icontains=query) |
            Q(moviedirectorassignment__director_director__director_last_name__icontains=query)
        ).distinct()
    else:
        results = Movie.objects.all()  # Or handle empty query as needed

    return render(request, 'results.html', {'results': results, 'query': query})