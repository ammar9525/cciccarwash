# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index2.html')
