from datetime import date

from django.shortcuts import render

from .models import Post

all_posts = [
    {
        "slug": "tech-music",
        "image": "music_tech.png",
        "author": "Brianny",
        "date": date(2026, 8, 5),
        "title": "Music Technology",
        "excerpt": "I like working on music with my DAW. I have a studio where I record different intruments and sounds for my songs.",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Brianny",
        "date": date(2026, 8, 5),
        "title": "Programming is cool",
        "excerpt": "I like solving problems. I don't mind the complexities programming has to offer. After all, it is like math in a way.",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        """
    },
    {
        "slug": "music-composition",
        "image": "music_software.png",
        "author": "Brianny",
        "date": date(2026, 8, 5),
        "title": "Composing Music",
        "excerpt": "Music is my passion. I write a lot of songs. I like to create melodies and different sounds using a music software",
        "content": """
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Tempora quia accusantium voluptatibus quibusdam error repellendus excepturi, in minus eligendi! Deserunt laudantium doloribus rem commodi laboriosam perspiciatis quaerat soluta, alias nam?

        """
    }    
]



# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
