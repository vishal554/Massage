from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'massage_app/index.html'
    
class AboutView(TemplateView):
    template_name = 'massage_app/about.html'
    
class ProductsView(TemplateView):
    template_name = 'massage_app/products.html'
    
class StoreView(TemplateView):
    template_name = 'massage_app/store.html'
    