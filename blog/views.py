from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def hello_world(request):
    context = {'artiles': Articles.objects.all(),
               'name': 'amir',
               'family': 'nazm'}
    return render(request, 'blog/hello_world.html', context)
