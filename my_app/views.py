from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, template_name='base.html')

def new_search(request):
    # pull data from search bar - was wir eintippen möchten wir auffangen
    search = request.POST.get('search') # das ist ein Python Dictionary get(für extrahieren) - weil POST Method dictionary liefert
    print(search) # double check in console ob wirklich ausgegeben wird wonach du gesucht hast
    # hier übergeben wir gleich werte für front-end
    stuff_for_front_end = {
        'search': search
    }
    return render(request, 'myapp/new_search.html', stuff_for_front_end)