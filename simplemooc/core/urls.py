from django.urls import path
from simplemooc.core.views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]