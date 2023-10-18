from django.urls import path
from . import views

urlpatterns= [
    path('register',views.register,name="register"),
    path('register_submit',views.register_submit,name="register_submit"),
    path('login',views.login,name="login"),
    path('login_submit',views.login_submit,name="login_submit"),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('change_password',views.change_password,name="change_password"),

]




