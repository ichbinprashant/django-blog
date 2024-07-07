from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post
from .forms import PostForm
from .forms import UserRegistrationForm

def post_list(request):
    # Retrieve all posts and paginate them, 5 per page
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    # Get a specific post by its primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # Set the author to the current logged-in user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'There was an error creating the post.')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # Prevent editing if not the author
    if request.user == post.author or request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Post updated successfully!')
                return redirect('post_detail', pk=post.pk)
            else:
                messages.error(request, 'There was an error updating the post.')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('post_detail', pk=post.pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author or request.user.is_superuser:
        if request.method == "POST":
            post.delete()
            messages.success(request, 'Post deleted successfully!')
            return redirect('post_list')
        return render(request, 'blog/post_delete.html', {'post': post})
    else:
        messages.error(request, 'You do not have permission to delete this post.')
        return redirect('post_detail', pk=post.pk)
