from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

from django.shortcuts import get_object_or_404
from .models import Movie, Actor, Director, Rating, Genre, Award, Gross, Casting, MovieDirectorAssignment, GenreMovieAssignment, MovieAwardAssignment
from .forms import MovieForm, GrossForm, ActorForm, DirectorForm, GenreForm, AwardForm
from django.contrib.auth.decorators import user_passes_test

import random
from .models import Movie
from .forms import GenreAwardSelectionForm
from .forms import ActorDirectorForm

#have to generate random id's because were using integer 
#value in database instead of django auto increment
def generate_unique_movie_id():
    while True:
        new_id = random.randint(100000, 999999) #six digits
        if not Movie.objects.filter(movie_id=new_id).exists(): #checks if id is already in database
            return new_id

def generate_unique_actor_id():
    while True:
        new_id = random.randint(100000, 999999) 
        if not Actor.objects.filter(actor_id=new_id).exists():
            return new_id

def generate_unique_director_id():
    while True:
        new_id = random.randint(100000, 999999)
        if not Director.objects.filter(director_id=new_id).exists():
            return new_id


def login_redirect(request):
    return redirect('login')  #to login page

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

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()


#added
def manage_movies(request):
    if request.method == 'POST': #what user submitted
        movie_form = MovieForm(request.POST)
        gross_form = GrossForm(request.POST)
        actor_director_form = ActorDirectorForm(request.POST)
        genre_award_form = GenreAwardSelectionForm(request.POST)

        if all([ #checks if respones are valid
            movie_form.is_valid(),
            gross_form.is_valid(),
            actor_director_form.is_valid(),
            genre_award_form.is_valid()
        ]):
            #movie
            movie = movie_form.save(commit=False) #dely for id generation
            movie.movie_id = generate_unique_movie_id() #generated id
            movie.save()

            #gross
            gross = gross_form.save(commit=False)
            gross.movie_movie = movie
            gross.save()

            #existing actors
            for actor in actor_director_form.cleaned_data['actors']:
                Casting.objects.create(actor_actor=actor, movie_movie=movie) #link actors to casting table

            #new actors
            new_actors_raw = actor_director_form.cleaned_data.get('new_actors', '')
            
            #actors names have to be parsed
            for name in [n.strip() for n in new_actors_raw.split(',') if n.strip()]: #split multiple actors apart
                parts = name.split() #split first and last name
                if len(parts) < 2: #skips if actor doesnt have first and last name enetered
                    continue
                first = parts[0].capitalize() #capitalize first name
                last = ' '.join(parts[1:]).title() #capitalize middle and last name
                last = ' '.join(parts[1:]).capitalize() #joins first and last name

                actor, created = Actor.objects.get_or_create( #checks for exisitng actors
                    
                    #no exisiting actor: create a new one
                    actor_first_name=first,
                    actor_last_name=last,
                    defaults={'actor_id': generate_unique_actor_id()}
                )

                if actor and actor.pk: #connect in casting table
                    Casting.objects.create(actor_actor=actor, movie_movie=movie)

            #connect existing directors to movie
            for director in actor_director_form.cleaned_data['directors']:
                MovieDirectorAssignment.objects.create(movie_movie=movie, director_director=director)

            #connect new directors to movie
            new_directors_raw = actor_director_form.cleaned_data.get('new_directors', '')
            for name in [n.strip() for n in new_directors_raw.split(',') if n.strip()]:
                parts = name.split()
                if len(parts) < 2:
                    continue
                first = parts[0].capitalize()
                last = ' '.join(parts[1:]).capitalize()

                director, created = Director.objects.get_or_create(
                    director_first_name=first,
                    director_last_name=last,
                    defaults={'director_id': generate_unique_director_id()}
                )

                if director and director.pk:
                    MovieDirectorAssignment.objects.create(movie_movie=movie, director_director=director)

            #connect genres (existing only) to movie : do not allow for new genres
            for genre in genre_award_form.cleaned_data['genres']:
                GenreMovieAssignment.objects.create(movie_movie=movie, genre_genre=genre)

            #connect awards (existing only) to movie : do not allow for new awards
            for award in genre_award_form.cleaned_data['awards']:
                MovieAwardAssignment.objects.create(movie_movie=movie, award_award=award)

            return redirect('manage_movies') #refreshes

    else:
        movie_form = MovieForm()
        gross_form = GrossForm()
        actor_director_form = ActorDirectorForm()
        genre_award_form = GenreAwardSelectionForm()

    all_movies = Movie.objects.all()

    return render(request, 'manage_movie.html', {
        'movie_form': movie_form,
        'gross_form': gross_form,
        'actor_director_form': actor_director_form,
        'genre_award_form': genre_award_form,
        'all_movies': all_movies,
    })


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) #get movie or error
    movie.delete() 
    return redirect('manage_movies') #refreshes

