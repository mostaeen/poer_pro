from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
