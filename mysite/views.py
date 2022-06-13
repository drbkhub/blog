from django.shortcuts import render


def about(request):
    return render(request, template_name='about.html')

def index(request):
    return render(request, template_name='index.html')
