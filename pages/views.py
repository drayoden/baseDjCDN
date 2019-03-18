#from django.shortcuts import render

from django.views.generic import TemplateView

# def index(request):
#     return render(request, 'pages/index.html')

class HomeView(TemplateView):
    template_name = 'pages/index.html'
