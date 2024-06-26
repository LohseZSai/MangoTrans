from django.urls import path

from django.conf import settings
from django.conf.urls. static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("callback/", views.callback, name="callback"),
    path("generic/", views.generic, name="generic"),
    path('profile/', views.profile, name='profile'),
    path('image-translator/', views.image_translator, name='image_translator'),
    path('pdf-translator/', views.pdf_translator, name='pdf_translator'),
    path('contact/', views.contact, name='contact'),
] + static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
