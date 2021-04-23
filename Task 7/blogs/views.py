from django.forms import forms
from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.core.exceptions import PermissionDenied
# Create your views here.


class BlogListView(ListView):
    model = post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin,CreateView):
    model= post 
    template_name = 'new_post.html'
    fields = ['title','body']
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.author
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = post
    template_name= 'post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model= post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied        
        return super().dispatch(request, *args, **kwargs)
    


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url =reverse_lazy('login')
    template_name = 'registration/signup.html'