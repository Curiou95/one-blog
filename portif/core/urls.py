from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('blog/', views.blog, name='blog_page'),
    path('projects/', views.projects, name='projects_page'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
]
