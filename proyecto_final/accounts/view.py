
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from proyecto_final.users.models import User


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