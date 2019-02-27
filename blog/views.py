from django.shortcuts import render
from django.utils import timezone
from .models import Post
def showform(request):
    return render(request,'blog/formtosearch.html')

def post_list(request):
    posts = Post.objects.filter(title__contains= request.GET['value'])
    return render(request, 'blog/post_list.html', {'posts': posts})