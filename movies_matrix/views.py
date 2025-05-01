from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.db.models import Search
from .models import Movie


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

    from django.shortcuts import render
    

def search_results(request):
    query = request.GET.get('search')
    if query:
            # Using icontains for case-insensitive search
        results = Movie.objects.filter(
            Search(title__icontains=query) | Search(author__icontains=query) | Search(description__icontains=query)
        )
    else:
        results = Movie.objects.all()  # Or handle empty query as needed

    return render(request, 'search_results.html', {'results': results, 'query': query})