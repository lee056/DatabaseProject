from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#url, view, template
urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('create-account/', views.create_account, name='create_account'),
    path('home/', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),

     
]
