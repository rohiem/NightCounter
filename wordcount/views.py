from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html", {"rohiem": "this is from home renders dictionary"})


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist= fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    wordsorted=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, "count.html", {"rohiem": "this is from counts renders dictionary", "fulltext": fulltext, "count": len(wordlist), "wordsorted": wordsorted})


def about(request):
    return render(request, "about.html", {"rohiem": "this is from about renders dictionary"})
