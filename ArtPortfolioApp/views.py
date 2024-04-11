
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
from .forms import ArtworkForm, PortfolioForm, ArtistForm
# Create your views here.

def index(request):
# Render index.html
    artwork_needs_adding=Artwork.objects.all().filter(needs_to_be_added=True).order_by('id')
    #print("artwork_needs_adding query set", artwork_needs_adding)
    return render( request, 'ArtPortfolioApp/index.html',{'artwork_needs_adding':artwork_needs_adding})

def stub(request):
   return render(request,"ArtPortfolioApp/stub.html")

class ArtistDetailView(DetailView):
    model=Artist
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["portfolios"] = Portfolio.objects.all().filter( Artist=context["object"].id )
       return context
   
class PortfolioDetailView(DetailView):
    model=Portfolio
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["artwork"] = Artwork.objects.all().filter( portfolio=context["object"].id )
       return context
class ArtworkDetailView(DetailView):
    model=Artwork

class ArtistListView(ListView):
    model=Artist
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class PortfolioListView(ListView):
    model=Portfolio
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ArtworkListView(ListView):
    model=Artwork
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def ArtworkAdd(request):
    submitted = False
    print(f"request{request}")
    if request.method == "POST":
      form=ArtworkForm(request.POST)
      print('Printing POST',request.POST)

      if form.is_valid():
          print("valid")
          form.save()
          return redirect('/ArtworkAdd?submitted=True') 
    else: 
        print("not valid")
        form=ArtworkForm()
        if 'submitted' in request.GET:
            submitted=True

    return render(request, "ArtPortfolioApp/create_artwork.html", {"form":form, 'submitted':submitted} )
    
def ArtworkEdit(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    form=ArtworkForm(request.POST or None,instance=artwork)
    if form.is_valid():
          form.save()
          return redirect('Artwork_list') 
    #https://www.geeksforgeeks.org/python-uploading-images-in-django/
    return render(request, "ArtPortfolioApp/edit_artwork.html",
                  {"form":form})

def ArtworkDelete(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    artwork.delete()
    return redirect('index')

def MarkAdded(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    artwork.needs_to_be_added=False
    artwork.save()
    return redirect('index')

def PortfolioCreate(request, Artist_id):
    artist=Artist.object.get(pk=Artist_id)
    form = PortfolioForm(request.POST)
    if form.is_valid():
          form.save()
          return redirect('/PortfolioCreate?submitted=True') 
    else: 
        form=ArtworkForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "ArtPortfolioApp/create_ArtPortfolio.html", {"form":form, 'submitted':submitted} )