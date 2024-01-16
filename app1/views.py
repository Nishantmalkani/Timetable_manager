from django.shortcuts import render

def demo1(request):
    return render(request,'index.html')

