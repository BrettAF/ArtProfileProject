
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
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

def index(request):
# Render index.html
    artwork_needs_adding=Artwork.objects.all().filter(needs_to_be_added=True).order_by('id')
    show_button= request.user.groups.all().filter(name='web-designer')
    #print("artwork_needs_adding query set", artwork_needs_adding)
    return render( request, 'ArtPortfolioApp/index.html',{'artwork_needs_adding':artwork_needs_adding, "show_button":show_button})

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

@login_required(login_url="login")
def ArtworkAdd(request):
    submitted = False
    if request.method == "POST":
      form=ArtworkForm(request.user, request.POST, request.FILES)


      if form.is_valid():
          print("valid")
          form.save()
          return redirect('index') 
    else: 
        print("not valid")
        form=ArtworkForm(request.user)
        if 'submitted' in request.GET:
            submitted=True

    return render(request, "ArtPortfolioApp/create_artwork.html", {"form":form, 'submitted':submitted} )

@login_required(login_url="login")    
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
    
@login_required(login_url="login")   
def ArtworkDelete(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    if artwork.portfolio.Artist.user == request.user:
        artwork.delete()
        
    return redirect('index')

@login_required(login_url="login")
@allowed_users(allowed_roles=["web-designer"])
def MarkAdded(request, Artwork_id):
    artwork=Artwork.objects.get(pk=Artwork_id)
    artwork.needs_to_be_added=False
    artwork.save()
    return redirect('index')

@login_required(login_url="login")
def PortfolioCreate(request):
    artist=Artist.objects.get(user=request.user)

    submitted = False
    form = PortfolioForm(request.POST)
    if form.is_valid():
        port= form.save(commit=False)
        port.Artist=artist
        print("*******************")

        port.save()
        return redirect('index') 
    else: 
        form=PortfolioForm()
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
            group=Group.objects.get(name='Artist')
            user.groups.add(group)
            artist = Artist.objects.create()
            artist.user=user
            artist.name= form.cleaned_data["artist_name"]
            artist.about_me = form.cleaned_data["about_me"]
            artist.save()
            
            messages.success(request,'Account was created for '+username)
            return redirect('index')
        
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


def logout_page(request):
    logout(request)
    return redirect( 'login')
    # Redirect to a success page.
    
    
    