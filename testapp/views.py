from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This response is from class Based Views</h1>')
class TemplateCBV(TemplateView):
    template_name = 'testapp/results.html'

class TemplateCBV2(TemplateView):
    template_name = 'testapp/results2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Adil'
        context['marks'] = 78
        context['subject'] = 'Python'
        return context