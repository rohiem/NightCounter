
def counts(request):
    fulltext = request 
    wordlist= list(fulltext.split())
    wordlila=['الليلة','ليالي','الليالي']
    wordcount=0
    for word in list(enumerate(wordlila)):
        wordcount+=wordlist.count(word[1])
        
    return wordcount
    
"""    ll=[]
    worddictionary=list(["الليالي",,""])
    for word in wordlist:
        for lil in worddictionary:
            if word == lil:
                ll.append(word)
            else:
                worddictionary=[]

"""
print(counts("الليلة الليلة الليالي الليالي ليالي ليالي الليلة يا الليلة الليلة الليالي الليالي ليالي ليالي الليلة سمرا"))