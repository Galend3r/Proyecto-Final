from django.urls import path
from proyecto_final.messages_blog.view import NewMessage, ListMessage


app_name = "messages"
urlpatterns = [
    path("", ListMessage.as_view() , name="listmessage"),
    path("new", NewMessage.as_view() , name="newmessage"),
]