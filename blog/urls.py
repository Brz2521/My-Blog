from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    # <slug:...> is a URL path converter used to capture a short, URL-friendly piece of text from a URL.
    path("posts/<slug:slug>", views.SinglePostView.as_view(), 
            name="post-detail"), #/posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")

]