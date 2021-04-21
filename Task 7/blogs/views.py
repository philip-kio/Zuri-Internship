from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


class BlogListView(ListView):
    model = post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model= post 
    template_name = 'new_post.html'
    fields = ['title','author','body']


class BlogUpdateView(UpdateView):
    model = post
    template_name= 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model= post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')