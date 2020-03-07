from .forms import PostForm
from .forms import ArticleForm
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Article
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


# View for articles
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_edit.html', {'form': form})


def article_detail(request,pk):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_detail.html', {'form': form})

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/article_list.html', {'articles':articles})

def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article = PostForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/article_edit.html', {'form': form})

def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# View for posts
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
	    form = PostForm(request.POST, request.FILES, instance=post)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.published_date = timezone.now()
	        post.save()
	        return redirect('post_detail', pk=post.pk)
	else:
	    form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')