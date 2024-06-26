from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()

        return context
class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data you need for the contact page
        return context