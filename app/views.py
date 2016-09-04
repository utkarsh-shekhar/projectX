from django.shortcuts import render

from django.views import generic
# Create your views here.
def IndexView(request):
    return render(request, 'app/index.html', { })
