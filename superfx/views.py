from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def about(request):
	return render(request, 'blog/about.html')
def home(request):
	return render(request, 'blog/home.html')
def contact(request):
	return render(request, 'blog/contact.html')
def htstart(request):
	return render(request, 'blog/htstart.html')
def deposits(request):
	return render(request, 'blog/deposits.html')
def ftraders(request):
	return render(request, 'blog/ftraders.html')