from django.urls import path
from theme.views import HomePage, About, Contact

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('apropos', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
]