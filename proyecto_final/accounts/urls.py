from django.urls import path
from proyecto_final.accounts.view import LoginView, RegisterView, ChangePassword, EditProfile, ProfileCreateUpdateView, ProfileView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


app_name = "accounts"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(template_name= "blog/home.html"), name="logout"),
    path("signup/", RegisterView.as_view(), name="singup"),
    path("password/", ChangePassword.as_view(), name="change_password"),
    path("edit_profile/", EditProfile.as_view(), name="edit_profile"),
    path("edit_avatar/", ProfileCreateUpdateView.as_view(), name="edit_avatar"),
    path("profile/", ProfileView.as_view(), name="profile"),
]