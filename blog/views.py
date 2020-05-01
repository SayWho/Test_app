from django.shortcuts import render, redirect
from .models import Post
from .forms import PostAddForm

def index(request):
    last_post = Post.objects.all()[:1]
    posts = Post.objects.all()[1:10]
    return render(request,
	          'blog/index.html',
              {'last_post' : last_post,
	          'posts': posts})

def new_post(request):
    form = PostAddForm()
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog')
    return render(request, 'blog/new_post.html', context={'form': form})