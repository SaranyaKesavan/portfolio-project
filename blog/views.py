from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    allblogs = Blog.objects.all().order_by('-published_date')
    return render(request,'blog/allblogs.html',{'allblogs':allblogs})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blogdetail})