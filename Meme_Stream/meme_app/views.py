from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def submitMeme(request):
    return render(request, 'meme_app/submitMeme.html')