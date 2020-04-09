from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.edit import FormMixin
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class homePage(TemplateView):
    template_name='blog/home.html'

class PostListView(ListView):
    context_object_name='post_list'
    model =Post
    def get_queryset(self):
        return Post.objects.filter().order_by('-created_date')

class PostDetailView(FormMixin,DetailView):
    context_object_name= 'post_detail'
    model=Post
    form_class=CommentForm
    def get_success_url(self):
        return reverse('blog:post_detail',kwargs={'pk':self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print('form_valid')
            return self.form_valid(form)
        else:
            print('form invalid')
            print(messages.error)
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)
    

class PostCreateView(CreateView):
    form_class=PostForm
    model = Post


class PostUpdateView(UpdateView):
    fields=('title', 'author', 'text')
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url=reverse_lazy('blog:post_list')
    template_name='blog/post_delete.html'


