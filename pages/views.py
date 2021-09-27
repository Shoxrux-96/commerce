from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from django.http.request import HttpRequest
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import Item,Order,Post

class HomePageView(TemplateView):
    template_name='home.html'
    def get(self, request):
        context = {
            'item':Item.objects.all(),
            'post': Post.objects.all(),
            }
        return render(request, self.template_name,context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ProductPage(TemplateView):
    template_name = 'watches.html'
    def get(self, request):
        context = {
            'order':Order.objects.all(),
            }
        return render(request, self.template_name,context)


class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'