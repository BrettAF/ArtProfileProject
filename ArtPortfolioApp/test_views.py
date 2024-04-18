from django.test import TestCase
from django.urls import reverse
from .models import Artwork, Portfolio, Artist
from django.contrib.auth.models import User
from django.test import Client
from .views import  ArtworkDelete

class ArtworkDeleteViewTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.artist1 = Artist.objects.create(user=self.user1, name='NAME',email = "EMAIL@EMAIL.com",about_me = "ABOUT ME",is_webdesigner=False)
        self.artist2 = Artist.objects.create(user=self.user2, name='NAME',email = "EMAIL@EMAIL.com",about_me = "ABOUT ME",is_webdesigner=False)
        self.portfolio1 = Portfolio.objects.create(Artist=self.artist1, title='Portfolio 1', description="DESCRIPTION",about = "ABOUT", contact_email = "EMAIL")
        self.portfolio2 = Portfolio.objects.create(Artist=self.artist2, title='Portfolio 2', description="DESCRIPTION",about = "ABOUT", contact_email = "EMAIL")
        self.artwork1 = Artwork.objects.create(title='Artwork 1', portfolio=self.portfolio1, description="DESCRIPTION", is_for_sale=False,  price="11111", needs_to_be_added=True,
            size_inches="SIZE", image='')
        self.artwork2 = Artwork.objects.create(title='Artwork 2', portfolio=self.portfolio2, description="DESCRIPTION", is_for_sale=False,  price="11111", needs_to_be_added=True,
            size_inches="SIZE", image='')


    def test_ArtworkDelete(self):
        client = Client()

        # Try to delete artwork1 as user2 (should fail)
        client.login(username='user2', password='password2')
        response = client.post(reverse(ArtworkDelete, args=[self.artwork1.id]))
        print("*****")
        print(self.artwork1.portfolio.Artist.user, client.get(User) )
        print(response.status_code)
        self.assertEqual(response.status_code, 302)  # Forbidden

        # Verify that artwork1 still exists
        self.assertTrue(Artwork.objects.filter(id=self.artwork1.id).exists())

        # Try to delete artwork2 as user2 (should succeed)
        response = client.post(reverse(ArtworkDelete, args=[self.artwork2.id]))
        print("*****")
        print(response.status_code)
        self.assertEqual(response.status_code, 302)  # Redirect after delete

        # Verify that artwork2 is deleted
        self.assertFalse(Artwork.objects.filter(id=self.artwork2.id).exists())