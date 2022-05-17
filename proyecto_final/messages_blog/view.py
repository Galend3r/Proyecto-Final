from multiprocessing import context
from django.views.generic import TemplateView
from .models import *
from .forms import MessageForms
from django.shortcuts import render

class NewMessage(TemplateView):
    template_name = 'message/new_message.html'

    def get(self, request):
        context = {
            'form': MessageForms(
                initial = {
                    'of': request.user.username,
                }
            )
        }

        return render(request, self.template_name, context)
    
    def post(self, request):

        Message.objects.create(
            from_message = request.user.username,
            to = request.POST.get('to'),
            message = request.POST.get('message'),
        )

        context = {
            'form': MessageForms()
        }

        return render(request, self.template_name, context)


class ListMessage(TemplateView):
    template_name = "message/list_messages.html"

    def get(self, request):

        context = {
            'messages': Message.objects.filter(to = request.user.username)
        }

        return render(request, self.template_name, context)