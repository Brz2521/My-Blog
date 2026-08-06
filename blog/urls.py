from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts"),
    # <slug:...> is a URL path converter used to capture a short, URL-friendly piece of text from a URL.
    path("posts/<slug:slug>", views.post_detail, name="post-detail") #/posts/my-first-post

]