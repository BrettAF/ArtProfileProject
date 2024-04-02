from django.forms import ModelForm
from django import forms

from .models import Artwork,Portfolio, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ["title","description","is_for_sale","price","size_inches","portfolio","image" ]

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title","contact_email","about", "description"]

#class CreateUserForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ["",]

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ["name","email"]