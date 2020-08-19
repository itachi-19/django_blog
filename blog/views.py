from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts =  [
    {
        'author': 'Itachi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27,2019'
    },
    {
        'author': 'Madara',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28,2019'
    },
]
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html',{'title': 'About'})
