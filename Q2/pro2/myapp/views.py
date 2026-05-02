from django.shortcuts import render,redirect,get_object_or_404
from .models import Post ,Comment
from .forms import PostForm,CommentForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post_list.html',{'posts':posts})

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request,'post_form.html',{'form':form})


def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,'post_confirm_delete.html',{'post':post})

def post_update(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request,'post_form.html',{'form':form})

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST )
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=pk)
    else:
        form = CommentForm()
    
    return render(request,'post_detail.html',{
        'post':post,
        'comments':comments,
        'form':form

    })

