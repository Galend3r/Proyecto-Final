from django.db import models
from proyecto_final.users.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

#python manage.py collectstatic para que poder usar el ckeditor luego de instalarlo con pip

class BlogPage(models.Model):
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    page_date = models.DateField(auto_now_add=True)

    