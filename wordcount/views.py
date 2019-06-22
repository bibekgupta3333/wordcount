from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    data= request.GET['fulltextarea']
    text=data.split()
    counted_text=len(text)

    worddictionary={}

    for word in text:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    sorted_list=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltextarea':data, 'len':counted_text,'worddictionary':sorted_list })