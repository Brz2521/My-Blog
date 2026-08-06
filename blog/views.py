from datetime import date

from django.shortcuts import render

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
    }    
]



# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
