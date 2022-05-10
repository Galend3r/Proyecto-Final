from django.db import models
from proyecto_final.users.models import User


class Profile(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile")