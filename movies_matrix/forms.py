from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie, Actor, Director, Rating, Genre, Award, Gross

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_title', 'release_year', 'duration', 'rating_rating']

class GrossForm(forms.ModelForm):
    class Meta:
        model = Gross
        fields = ['domestic_gross', 'international_gross']

class ActorForm(forms.ModelForm):
    existing_actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.order_by('actor_last_name'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Actor
        fields = ['actor_first_name', 'actor_last_name']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['director_first_name', 'director_last_name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['award_name']
        
#for manage movies
class GenreAwardSelectionForm(forms.Form): #get input from user
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(), #query database to get all genres
        required=True,
        widget=forms.CheckboxSelectMultiple, #shows as a textbox 
        label="Genres"
    )

    awards = forms.ModelMultipleChoiceField(
        queryset=Award.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Awards"
    )

#for manage movies
class ActorDirectorForm(forms.Form): #
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.order_by('actor_last_name'), #query database to get all actors sorted by last name
        required=False,
        widget=forms.CheckboxSelectMultiple, #textboxes
        label="Existing Actors"
    )
    new_actors = forms.CharField(
        required=False,
        help_text="Add new actors (format: First Last, First Last)", #shpws up uder textbox
        widget=forms.TextInput(attrs={"placeholder": "e.g. Tom Hanks, Emma Stone"}) #shows how to use textbox
    )

    directors = forms.ModelMultipleChoiceField(
        queryset=Director.objects.order_by('director_last_name'),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Existing Directors"
    )
    new_directors = forms.CharField(
        required=False,
        help_text="Add new directors (format: First Last, First Last)",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Greta Gerwig, Steven Spielberg"})
    )

