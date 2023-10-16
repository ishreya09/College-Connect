from django.urls import path
from . import views

urlpatterns= [
    path('', views.home,name= 'home'),
    path('privacy-policy',views.privacypolicy,name="privacypolicy"),
    path('contact-us',views.contact_us,name="contactus"),
]




