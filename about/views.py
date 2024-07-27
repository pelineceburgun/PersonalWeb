from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Page
from .forms import PostForm
# Create your views here.
def home(request):
    return  render(request,'about/home.html')
def about(request):
    return render(request,'about/about.html')
def portfolio(request):
    return render(request,'about/portfolio.html')
def contact(request):
    return render(request,'about/contact.html')

def references_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('references')
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, 'about/references.html', {'form': form, 'posts': posts})

def search_all(request):
    query = request.GET.get('q')
    post_results = Page_results = []

    if query:
        post_results = Post.objects.filter(title__icontains=query)
        page_results = Page.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'post_results': post_results,
        'page_results': page_results,
    }
    return render(request, 'about/search_results.html', context)
