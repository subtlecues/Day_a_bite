from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("home/", views.index, name="index"),
    path("register_user/", views.registration_handler, name='registration_handler'),
    path("login/", views.login_handler, name="login"),
    path("logout/", views.logout_handler, name="logout"),
    path("my-measurements/", views.my_measurements_view, name="my-measurements"),
    path("my-profile/", views.my_profile_view, name="my-profile"),
    path("encyclopedia/", views.encyclopedia_view, name="encyclopedia"),
]
