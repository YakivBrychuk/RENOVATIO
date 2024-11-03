from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# List view for posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

# Detail view for a single post
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All comments related to the post, ordered by creation date (descending).
    ``comment_count``
        Count of approved comments for the post.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Retrieve and order comments, count approved comments
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_details.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )
