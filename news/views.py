from django.shortcuts import render
from urllib.request import urlopen as uReq
from bs4 import  *
from bs4 import BeautifulSoup as soup


def news(request):

    my_url = 'https://www.newsx.com/regional'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    val = page_soup

    # Gets Each headings
    headings = page_soup.findAll("div", {"class": "caption"})
    #container = headings[0]
    for container in headings:
        linkval = (container.a['href'])

# Create your views here.
#def news(request):
        return render(request, 'news/news.html', {'user': linkval})

