from django.forms import ModelForm
from django import forms

from .models import Artwork,Portfolio, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ["title","description","is_for_sale","price","size_inches","portfolio","image" ]
        labels = {"title":'The artworks name',
                  "description":"describe your Artwork",
                  "is_for_sale":"Is this piece for sale",
                  "price":"Price",
                  "size_inches":"Size in Inches",
                  "portfolio":"What Portfolio is it in?",
                  "image":"Upload your image"
                  }
        widgets= {"title":forms.TextInput(attrs={'class':'form_control'}),
                  "description":forms.TextInput(attrs={'class':'form_control'}),
                  "price":forms.TextInput(attrs={'class':'form_control'}),
                  "size_inches":forms.TextInput(attrs={'class':'form_control'}),
                }
            
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "description"]

#class CreateUserForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ["",]

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ["name","email"]
        
