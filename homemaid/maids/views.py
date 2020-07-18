# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Maid

class MaidListView(View):
    def get(self, request):
        html = ''
        for m in Maid.objects.all():
            html += f'<li>{m.name}</li>'
        return HttpResponse(html)
    