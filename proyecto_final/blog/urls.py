from django.urls import path
from proyecto_final.blog.view import CreateBlogPage, UpdateBlogPage, DeleteBlogPage


app_name = "pages"
urlpatterns = [
    path("create/", CreateBlogPage.as_view() , name="create"),
    path("edit/<int:pk>", UpdateBlogPage.as_view(), name="edit"),
    path("delete/<int:pk>", DeleteBlogPage.as_view(), name="delete"),
]