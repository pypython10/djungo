from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')





    #return HttpResponse ("<h65>Hello python</h65>")#from django.http import HttpResponse