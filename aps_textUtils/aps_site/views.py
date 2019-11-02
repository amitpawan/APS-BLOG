#File Created by APS
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def analyze(request):
    fetch_text=request.POST.get('text','default')
    fetch_removePunc=request.POST.get('removepunc','off')   
    fetch_uppercase=request.POST.get('uppercase','off')   
    fetch_newlineremover=request.POST.get('newlineremover','off')      
    fetch_extraspaceremover=request.POST.get('extraspaceremover','off')      
    fetch_charactercounter=request.POST.get('charactercounter','off')      
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    formatted_text=""
    if fetch_removePunc=='on':
        for char in fetch_text:
            if char not in punctuations:
                formatted_text=formatted_text+char 
        params={'purpose':'Remove Puntuations','after_text':formatted_text}           
        fetch_text=formatted_text
    if(fetch_uppercase=='on'):
        formatted_text=""
        for char in fetch_text:
            formatted_text=formatted_text+char.upper()
        params={'purpose':'UPPERCASE','after_text':formatted_text}           
        fetch_text=formatted_text
    if(fetch_newlineremover=='on'):
        formatted_text=""
        for char in fetch_text:
            if (char!="\n" and char!="\r"):
                formatted_text=formatted_text+char
        params={'purpose':'New Line Removed','after_text':formatted_text}           
        fetch_text=formatted_text
    if(fetch_extraspaceremover=='on'):
        formatted_text=""
        for index,char in enumerate(fetch_text):
            if not(fetch_text[index]==" " and fetch_text[index+1]==" "):
                formatted_text=formatted_text+char
        params={'purpose':'Extra Space Removed','after_text':formatted_text}           
        fetch_text=formatted_text
    if(fetch_charactercounter=='on'):
        formatted_text=0
        for index,char in enumerate(fetch_text):
            if fetch_text[index]!=" ":
                formatted_text=formatted_text+1
        params={'purpose':'Total Characters excluding spaces','after_text':formatted_text}
    if(fetch_removePunc!='on' and fetch_uppercase!='on' and fetch_newlineremover!='on' and fetch_extraspaceremover!='on' and fetch_charactercounter!='on'):
        return HttpResponse('ERROR ! It seems you didnot selected any of the actions')    

                         
    return render(request,"removePunc.html",params)        










