
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from proyecto_final.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from proyecto_final.accounts.forms import UserCreationFormCustom, UserChangeFormCustom, ProfileForms
from proyecto_final.accounts.models import Profile


class LoginView(TemplateView):
    template_name = 'blog/account/login.html'

    def get(self, request):
        context = {
            'form' : AuthenticationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form:
            user = request.POST.get('username')
            password = request.POST.get('password')

            user_auth = authenticate(username = user, password = password)

            if user_auth:
                login(request, user_auth)
                #return redirect('')
                return render(request, self.template_name, context={'message': f'Bienvenido {user}'})
            else:
                return render(request, self.template_name, context={'message': f'Usuario Invalido'})

        else:
            return render(request, self.template_name, context={'message': f'Formulario errado'})

class RegisterView(TemplateView):
    template_name = 'blog/account/signup.html'

    def get(self, request):
        context = {
            'form' : UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationFormCustom(request.POST)

        if form:
            form.save()
            return render(request, self.template_name, context={'message': f'Usuario registrado correctamente'})
        else:
            return render(request, self.template_name, context={'message': f'Ocurrio un error'})

class ChangePassword(PasswordChangeView):
    model = PasswordChangeView 
    template_name = 'blog/account/change_password.html'
    success_url = "/"

class EditProfile(LoginRequiredMixin, TemplateView):
    template_name = 'blog/account/edit_profile.html'

    def get(self, request):
        context = {
            'form' : UserChangeFormCustom(
                initial = {
                    'first_name' : request.user.first_name,
                    'last_name' : request.user.last_name,
                    'email' : request.user.email,
                    'name' : request.user.name
                }
            )
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserChangeFormCustom(request.POST)
        if form.is_valid():
            user_update_info = form.cleaned_data
            user = request.user
            user.name = user_update_info.get('name')
            user.email = user_update_info.get('email')
            #user.username = user_update_info.get('username')
            user.first_name = user_update_info.get('first_name')
            user.last_name = user_update_info.get('last_name')
            #user.password1 = user_update_info.get('password1')
            #user.password2 = user_update_info.get('password2')
            user.save()

        context = {
            'form' : UserChangeFormCustom(
                initial = {
                    'first_name' : request.user.first_name,
                    'last_name' : request.user.last_name,
                    'email' : request.user.email,
                    'name' : request.user.name
                }
            )
        }
        
        return render(request, self.template_name, context)

class ProfileCreateUpdateView(TemplateView):
    template_name = 'blog/account/edit_avatar.html'

    def get(self, request):

        profile = Profile.objects.filter(user=request.user.id)

        if profile:
            context = {
                'form' : ProfileForms(
                    initial = {
                        'bio' : profile[0].bio,
                        'link' : profile[0].link,
                        'profile_image' : profile[0].profile_image,
                    }
                )
            }
        else:
            context = {
                'form' : ProfileForms()
            }
        
        return render(request, self.template_name, context)

    def post(self, request):

        miformulario = ProfileForms(request.POST, request.FILES)

        if miformulario.is_valid():

            Profile.objects.update_or_create(
                user=request.user,
                defaults={
                    'bio' : miformulario.cleaned_data['bio'],
                    'link' : miformulario.cleaned_data['link'],
                    'profile_image' : miformulario.cleaned_data['profile_image'],
                }
            )
        self.template_name = 'blog/account/profile.html'
        profile = Profile.objects.filter(user=request.user.id)

        context = {
                'form' : ProfileForms(
                    initial = {
                        'bio': profile[0].bio,
                        'link': profile[0].link,
                        'profile_image': profile[0].profile_image,
                    }
                )
            }
        return render(request, self.template_name, context)
        

class ProfileView(TemplateView):
    template_name = 'blog/account/profile.html'

    def get(self, request):

        profile = Profile.objects.filter(user=request.user.id)


        if profile:
            context = {
                'bio' : profile[0].bio,
                'link' : profile[0].link,
                'profile_image' : profile[0].profile_image,
            }
        else:
            context = {
                'bio' : "",
                'link' : "",
                'profile_image' : "",
            }

        return render(request, self.template_name, context)