from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from html import escape
from .models import Post
from django.urls import reverse
# Create your views here.


def homepage(request):
    return HttpResponse("<h1>Hello Everyone</h1>")

def say_hi(request, name):
    msg = """
    <html>
        <body>
            <p>Hello """ + escape(name) + """
            </p>
        </body>
    </html>
    """
    # msg = "<script>alert('some content')</script>"
    return HttpResponse(msg)

def get_post(request, id):
    requested_post = Post.objects.filter(id=id)
    return render(request, 'blog/timeline.html', {
        'posts': requested_post
    })
    
def get_all_posts(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/timeline.html', context)

def delete_post(request, id):
    requested_post = Post.objects.filter(id=id)
    requested_post.delete()
    return HttpResponseRedirect(reverse('homepage'))

# normal:
# 'http:127.0.0.1:8000/blog/say_hi/' -> say_hi

# revese:
# 'http:127.0.0.1:8000/blog/say_hi/' <- say_hi
