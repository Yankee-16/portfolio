from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Max
from django.contrib import messages
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
def all(request):
    post = Post.objects.order_by('pub_date')
    return render(request, 'blog/all_blogs.html', {'post': post})

def detail(request, slug):
    print(slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

@login_required
def post(request):
    print('Here')
    if request.user.is_superuser == 0:
        return HttpResponseRedirect(reverse('all'))
    # form = PostForm(request.POST or None)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('blog:all'))
        else:
            print("Invalid Data")
            return HttpResponseRedirect(reverse('post'))
    else:
        form = PostForm()
        return render(request, 'blog/post.html', {'form': form})
