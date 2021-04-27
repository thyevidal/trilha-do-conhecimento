from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    context = {
        'blog' : Post.objects.all(),
    }
    return render(request, 'index.html', context)

def blog(request):
    post = {
        'post' : Post.objects.all(),
    }
    return render(request, 'blog.html', post)