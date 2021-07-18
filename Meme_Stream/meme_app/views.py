from django.db import models
from django.db.models.base import Model
from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def home(request):
    memeData = models.MemeInfo.objects.all()
    date = models.MemeInfo.objects.order_by('-created')
    # a = models.MemeInfo.objects.get(id=29)
    print(date)

    return render(request, 'base.html')

def openEditForm(request):
    return render(request, 'meme_app/editMeme.html')

def search(request):
    searchElement = request.POST.get('searchObject')
    id = models.MemeInfo.objects.get(id=searchElement)

    searchResultData = []
    if models.MemeInfo.objects.filter(id=searchElement).exists():
        print(id.nameOfMemeOwner)
        searchResultData.append((id.nameOfMemeOwner, id.caption, id.memeUrl))
    else:
        Http404('Id does\'nt exists, Try again')

    resultToShow ={
        'id':searchElement,
        'searchResultData': searchResultData,
    }
    return render(request, 'meme_app/searchResults.html', resultToShow)

# for streaming the posted memes
def stream(request):
    memeData = models.MemeInfo.objects.order_by('-created')
    data = []
    for memers in memeData:
        name = memers.nameOfMemeOwner
        caption = memers.caption
        imgUrl = memers.memeUrl
        memeId = memers.id
        print(memers.id)
        data.append((name, caption, imgUrl, memeId))
    stream_data = {
        'data': data,
    }
    # print(stream_data['data'])
    return render(request, 'meme_app/streamPage.html', stream_data)

# Only for opening the submit form
def openForm(request):
    return render(request, 'meme_app/submitMeme.html')

def submitMeme(request):
    memerName = request.POST.get('memerName')
    caption = request.POST.get('caption')
    memeURL = request.POST.get('memeURL')
    # print(memerName, caption, memeURL)

    if request.POST.get('memerName') and request.POST.get('memeURL'):
        models.MemeInfo.objects.create(nameOfMemeOwner=memerName, caption=caption, memeUrl=memeURL)

    return render(request, 'meme_app/submitMeme.html')

def editMeme(request):
    newCaption = request.POST.get('newCaption')
    newMemeUrl = request.POST.get('newMemeURL')
    memeId = request.POST.get('memeId')

    if models.MemeInfo.objects.filter(id=memeId).exists():
        if newCaption and newMemeUrl:
            meme = models.MemeInfo.objects.get(id=memeId)
            meme.caption = newCaption
            meme.memeUrl = newMemeUrl
            meme.save()
        elif newCaption and not newMemeUrl:
            meme = models.MemeInfo.objects.get(id=memeId)
            meme.caption = newCaption
            meme.save()
        elif not newCaption and newMemeUrl:
            meme = models.MemeInfo.objects.get(id=memeId)
            meme.memeUrl = newMemeUrl
            meme.save()
        elif not newCaption and not newMemeUrl:
            raise Http404('Please fill atleast any of one field you want to edit! 😐')
        else:
            raise Http404('Something went wrong! Try again... 😥')
            
        # meme = models.MemeInfo.objects.get(id=memeId)
        # meme.caption = newCaption
        # meme.memeUrl = newMemeUrl
        # meme.save()
    else:
        return HttpResponseNotFound('<h1>Woops, Meme Id not found! 🚫</h1>')
        

    print(models.MemeInfo.objects.filter(id=memeId).exists())
    
    return render(request, 'meme_app/streamPage.html')