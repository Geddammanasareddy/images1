from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'manasa','l':[11,12,13,14]}
    return render(request,'looping.html',d)
