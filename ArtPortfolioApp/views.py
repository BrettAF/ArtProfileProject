
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
from .forms import ArtworkForm, PortfolioForm, ArtistForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import logout

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
    print(submitted)
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

def ArtworkView(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    return render((request, 'display_artwork.html',
                       {'Artwork_images': artwork}))
    
    
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
    artist=Artist.objects.get(pk=Artist_id)
    submitted = False
    form = PortfolioForm(request.POST)
    if form.is_valid():
          form.save()
          return redirect('/PortfolioCreate?submitted=True') 
    else: 
        form=ArtworkForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "ArtPortfolioApp/create_ArtPortfolio.html", {"form":form, 'submitted':submitted} )


def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('index')
     
    # Render the login page template (GET request)
    return render(request, 'ArtPortfolioApp/login.html')

def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            #group=Group.objects.get(name='artist')
            #user.groups.add(group)
            artist = Artist.objects.create(user=user)
            #artist.objects.name=
            artist.save()
            
            messages.success(request,'Account was created for '+username)
            return redirect('ArtPortfolioApp/Artist_create')
        
    context = {'form':form}
    return render( request,'ArtPortfolioApp/registration/register.html', context)

def ArtistCreate(request):
    form=ArtistCreate
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            artist=form.save()
            
            messages.success(request,'Account was created for ')
            return redirect('login')
    return redirect('ArtPortfolioApp/Artist_create')
    from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return('ArtPortfolioApp/login')
    # Redirect to a success page.