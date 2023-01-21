from django.contrib import admin
from django.urls import path,include
from home import views




# Django admin header customisation
admin.site.site_header = "Developer Ashima"
admin.site.site_title="Welcome to Ashima Dashboard"
admin.site.index_title="welcome to this portal"


urlpatterns = [

    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('project',views.project, name='project'),

]