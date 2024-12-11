from django.http import HttpResponse
from django.shortcuts import render ,redirect
import operator

def home(request):
    return render(request, "home.html", {"rohiem": "this is from home renders dictionary"})

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist= fulltext.split()
    worddictionary={}
    wordsorted=[]
    if "count" in request.GET:
#        wordcount=wordlist.count("بالليل")+wordlist.count("ياليل")+wordlist.count("ليل،")+wordlist.count("ليلي،")+wordlist.count("الليالي")+wordlist.count("ليالي")+wordlist.count("الليلة")+wordlist.count("ليلة")+wordlist.count("الليل")+wordlist.count("ليل")+wordlist.count("ليلي")+wordlist.count("والليلة")+wordlist.count("الليله")+wordlist.count("والليله")+wordlist.count("ليله")
#       [ "بالليل","ياليل","ليل،","ليلي،","الليالي","ليالي","الليلة","ليلة","الليل","ليل","ليلي","والليلة","الليله","والليله","ليله"]

        wordlila=[ "بالليل","ياليل","ليل،","ليلي،","الليالي","ليالي","الليلة","ليلة","الليل","ليل","ليلي","والليلة","الليله","والليله","ليله"]
        wordcount=0
        for word in list(enumerate(wordlila)):
            wordcount+=wordlist.count(word[1])
        
        context= {"rohiem": "this is from counts renders dictionary", "fulltext": fulltext, "count": len(wordlist), "wordsorted": wordsorted,"wordcount":wordcount}
        return render(request, "count.html",context)

    elif "sort"  in request.GET:

        for word in wordlist:
            if word in worddictionary:
                worddictionary[word]+=1
            else:
                worddictionary[word]=1
        wordsorted=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
        wordcount=0
        context= {"rohiem": "this is from counts renders dictionary", "fulltext": fulltext, "count": len(wordlist), "wordsorted": wordsorted,"wordcount":wordcount}
        return render(request, "counts.html",context)
    else :
        return redirect("home/")
        

def about(request):
    return render(request, "about.html", {"rohiem": "this is from about renders dictionary"})
"""
def counts(request):
    fulltext = request 
    wordlist= list(fulltext.split())
    wordcount=wordlist.count("الليالي")+wordlist.count("ليالي")+wordlist.count("الليلة")+wordlist.count("بالليل")+wordlist.count("فالليل")+wordlist.count("كالليل")+wordlist.count("والليلة")+wordlist.count("ليلة")+wordlist.count("كالليلة")+wordlist.count("فالليلة")
    return wordcount
  
def countlila(request):
    fulltext = request.GET["fulltext"]
    wordlist= list(fulltext.split())
    wordcount=wordlist.count("الليالي")+wordlist.count("ليالي")+wordlist.count("الليلة")
    return render(request, "lila.html",{"wordcount":wordcount, "fulltext": fulltext}) 
"""