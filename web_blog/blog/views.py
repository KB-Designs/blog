from django.shortcuts import render, get_list_or_404
from  .models import Post

def post_list(request):
   
    return render(request, 'blog/post/list.html')

def about(request):
    return render(request, 'blog/post/detail.html')

# Create your views here.
