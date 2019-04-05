from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
# Create your views here.


class Index(View):
    def get(self, request):
        return HttpResponse('This is where my views stuff will populate!!! GET GET GET IT!!!')

    def post(self, request):
        return HttpResponse('This is where my views stuff will populate!!! POST POST POST!!!')
