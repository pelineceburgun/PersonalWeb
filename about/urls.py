from django.urls import path

from about import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('references/', views.references_view, name='references'),
    path('search/', views.search_all, name='search_all'),

]