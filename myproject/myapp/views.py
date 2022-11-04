# Create your views here.

from multiprocessing import context
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from .form import PostForm

class Index(TemplateView):
    template_name='myapp/index.html'

# 8行目　myapp/indexの
# /はフォルダの中の何か（ファイルとかフォルダ）を参照
# .はファイルの中の関数参照

    def get_context_data(self,*args, **kwargs) :
        context = super().get_context_data
        post_list= Post.objects.all().order_by('-created_at')
        context={'post_list':post_list,}
        return context




# CreateViewとかDetailViewとかはhtmlに行けよってことも含んでいる。
# 私たちが膨大に記述するべきものがここに入っている。

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('myapp:index')

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    def get_success_url(self):

        return resolve_url('myapp:post_detail', pk=self.kwargs['pk'])

class PostDelete(DeleteView):
    model = Post

    def get_success_url(self):

        return resolve_url('myapp:index')