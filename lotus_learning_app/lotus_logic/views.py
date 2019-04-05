from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
# Create your views here.


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Testing out...should see some text here.'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('This is where my views stuff will populate!!! POST POST POST!!!')
