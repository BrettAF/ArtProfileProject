from django.db import models
from django.urls import reverse


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
    

class Portfolio(models.Model):
    title= models.CharField("title", max_length=200)
    contact_email= models.CharField("contact_email", max_length=200)

    about=models.CharField("About this portfolio", max_length=2000)
    Artist= models.ForeignKey(Artist, on_delete=models.CASCADE)
    description=models.CharField("Description of the model", max_length=1000)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])
    
    
class Artwork(models.Model):
    title= models.CharField("title", max_length=200)
    description=models.CharField("Description",max_length=2000)
    is_for_sale=models.BooleanField()
    price=models.FloatField()
    needs_to_be_added=models.BooleanField(default=True)
    size_inches=models.CharField("size in inches", max_length=200)
    image=models.ImageField(upload_to='images/')
    portfolio= models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])