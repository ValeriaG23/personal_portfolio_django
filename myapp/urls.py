from django.urls import path
from .views import HomeTemplateView, ContactTemplateView
from django.conf.urls.static import static
from appwebavans import settings

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)