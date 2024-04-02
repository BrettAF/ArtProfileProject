from django.urls import path
from . import views
urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('login',views.stub,name='login'),
path('logout',views.stub,name='logout'),

path('portfolio_list', views.ArtistListView.as_view(),name="portfolio-list"),
path('artist_list', views.ArtistListView.as_view(),name="artist-list"),
path('artwork_list', views.ArtworkListView.as_view(),name="artwork-list"),




]