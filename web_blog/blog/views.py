from django.shortcuts import render
from  .models import Post

def home(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/post/list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/post/detail.html')

# Create your views here.
