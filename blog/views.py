from django.shortcuts import render
from django.http import HttpResponse
from html import escape
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