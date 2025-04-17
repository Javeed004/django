from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request, 'login.html')


def newView(request):
    return render(request, 'new.html')