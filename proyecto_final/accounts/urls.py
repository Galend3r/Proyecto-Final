from django.urls import path
from proyecto_final.accounts.view import LoginView, RegisterView
from django.contrib.auth.views import LogoutView



app_name = "accounts"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(template_name= "blog/home.html"), name="logout"),
    path("signup/", RegisterView.as_view(), name="singup"),
    # path("profile/", , name="profile"),
]