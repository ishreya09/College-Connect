from django.urls import path
from . import views

urlpatterns= [
    path('feed', views.feed,name= 'feed'),
    path('make_post',views.make_post,name='make_post'),
    path('<slug>',views.post_detail,name='post_detail'),    
    path('add-comment/<slug>',views.add_comment,name='comment_on_post'),
]




