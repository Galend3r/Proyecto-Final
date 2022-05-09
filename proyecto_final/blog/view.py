from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

class ListBlogPage(ListView):
    model = BlogPage
    template_name = "blog/list_pages.html"
    ordering = ['-page_date']

class DetailBlogPage(DetailView):
    model = BlogPage
    template_name = "blog/detail_page.html"

class CreateBlogPage(CreateView):
    model = BlogPage
    template_name = 'blog/create_page.html'
    success_url = "/"
    fields = '__all__'

class UpdateBlogPage(UpdateView):
    model = BlogPage
    template_name = 'blog/edit_page.html'
    success_url = "/"
    fields = '__all__'

class DeleteBlogPage(DeleteView):
    model = BlogPage
    template_name = 'blog/delete_page.html'
    success_url = "/"