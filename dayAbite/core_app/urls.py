from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register_user/", views.registration_handler, name='registration_handler'),
    path("login", views.login_handler),
    path("logout", views.logout_handler)
]
