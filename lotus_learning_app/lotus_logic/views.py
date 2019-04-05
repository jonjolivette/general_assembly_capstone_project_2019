from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
# Create your views here.


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Testing out...should see some text here for a dynamic variable executed in a function called when we hit the Index route with a GET request I created in views.py verses executing an entire template.'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('This is where my views stuff will populate!!! POST POST POST!!!')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'I\'m a New Video'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('This is where my views stuff will populate!!! POST POST POST!!!')
