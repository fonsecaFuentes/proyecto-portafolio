from django.shortcuts import render
# from django.shortcuts import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request, 'core/contact.html')
