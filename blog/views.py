from datetime import date
from django.shortcuts import render
from blog.models  import Post
from django.shortcuts import get_object_or_404

all_posts = [
]


def gen_date(all_posts):
    return all_posts["date"]


# Create your views here.
def starting_page(request):
    lates_posts=Post.objects.all().order_by('-date')[:2]
    return render(request, "blog/index.html", {"posts": lates_posts})


def posts(request):
    all_posts=Post.objects.all()
    return render(request, "blog/all-posts.html",{
        'posts':all_posts
    })


def post_detail(request, slug):
    # post=get_object_or(Post.objects.get(slug=slug))
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",{
        'post':post,
        "tags":post.tag.all()
    })
