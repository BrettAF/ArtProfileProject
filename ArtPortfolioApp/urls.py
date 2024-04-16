from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('login',views.login_page,name='login'),
path('logout',views.logout_view,name='logout'),
path('register',views.registerPage,name='register'),

path('Portfolio_list/', views.PortfolioListView.as_view(), name="Portfolio_list"),
path('Artist_list/', views.ArtistListView.as_view(), name="Artist_list"),
path('Artwork_list/', views.ArtworkListView.as_view(), name="Artwork_list"),

path('Portfolio_detail/<pk>', views.PortfolioDetailView.as_view(), name="Portfolio_detail"),
path('Artwork_detail<pk>', views.ArtworkDetailView.as_view(), name="Artwork_detail"),
path('Artist_detail<pk>', views.ArtistDetailView.as_view(), name="Artist_detail"),

path('Artwork_add', views.ArtworkAdd,name="Artwork_add"),
path('Artwork_edit<Artwork_id>',views.ArtworkEdit, name='Artwork_edit' ),
path('Artwork_delete<Artwork_id>', views.ArtworkDelete, name='Artwork_delete'),
path('Artwork_mark_added<Artwork_id>', views.MarkAdded, name='Artwork_mark_added'),

path('Portfolio_create',views.PortfolioCreate, name="Portfolio_create"),
path('Artist_create<user_id>', views.ArtistCreate,name="Artist_create"),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)