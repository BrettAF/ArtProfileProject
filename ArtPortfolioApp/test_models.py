from django.test import TestCase
from .models import *

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='test_user', email='test@example.com')
        Artist.objects.create(name='NAME',
            email = "EMAIL@EMAIL.com",
            about_me = "ABOUT ME",
            is_webdesigner=False,
            user = user)

    def test_name_label(self):
        artist =Artist.objects.get(id=1)
        field_label = artist._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')


    def test_first_name_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        artist = Artist.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(artist.get_absolute_url(), '/Artist_detail1')
















