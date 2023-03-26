# vivek is the bosss
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    
    # return HttpResponse("HOME <a href='http://127.0.0.1:8000/removepunc'>removepunc<a/>")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(djtext)
    print(removepunc)
    # analyzed = djtext:
    if removepunc == "on":
        punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capitalized Letters', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif(charcounter=="on"):
        analyzed=0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose':'Capitalized Letters', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")