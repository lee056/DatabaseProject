from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm



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

