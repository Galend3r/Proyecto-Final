from attr import field
from django import forms
from proyecto_final.users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from proyecto_final.accounts.models import Profile
from django.db import models


class ProfileForms(forms.Form):
    bio = forms.CharField(required=False)
    link = forms.CharField(required=False)
    profile_image = forms.ImageField(allow_empty_file=True)

    class Meta:
        model = Profile
        fields = ('bio', 'link','profile_image')

#modifique la class Meta en forms.py de django.contrib linea 98 agrego campo email y en la clase UserCreationFormCustom agreo el campo para que guarde el dato
class UserCreationFormCustom(UserCreationForm):
    
    def save(self, commit: bool = True) -> User:
        print(self.__dict__)
        user = User.objects.create(
            username =  self.data['username'],
            password =  self.data['password1'],
            email = self.data['email'],
        )
        return user

class UserChangeFormCustom(UserChangeForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('name', 'first_name', 'last_name','email', 'username')
