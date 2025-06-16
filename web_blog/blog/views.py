from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Post
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm




def home(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/post/list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/post/detail.html')

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('autheticated'\
                                        'successfully')
                else:
                    return HttpResponse('Diabled account')
            else:
                return HttpResponse('Invalid login')  
    else:
        form=LoginForm()
    return render(request, 'blog/authentication/login.html', {'form':form})              
    

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Set password properly
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Redirect to login page after successful registration
            return redirect('login')  # Make sure you have a URL named 'login'
        # If form is invalid, fall through to render with errors
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'blog/authentication/register.html', {'user_form': user_form})

