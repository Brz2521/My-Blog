from datetime import date

from django.shortcuts import render

posts = [
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

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
