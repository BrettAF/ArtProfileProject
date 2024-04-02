from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
#from .forms import ProjectForm, PortfolioForm, StudentForm 
# Create your views here.

def index(request):
# Render index.html
    artwork_needs_adding=Artwork.objects.all().filter(needs_to_be_added=True)
    #print("artwork_needs_adding query set", artwork_needs_adding)
    return render( request, 'ArtPortfolioApp/index.html',{'artwork_needs_adding':artwork_needs_adding})

def stub(request):
   return render(request,"ArtPortfolioApp/stub.html")

class ArtistDetailView(DetailView):
    model=Artist
class PortfolioDetailView(DetailView):
    model=Portfolio
class ArtworkDetailView(DetailView):
    model=Artwork
class ArtistListView(ListView):
    model=Artist
class PortfolioListView(ListView):
    model=Portfolio
class ArtworkListView(ListView):
    model=Artwork

def update_Artwork(request, Artwork_id):
    form=ArtworkForm()
    artwork=artwork.objects.get(pk=Artwork_id)