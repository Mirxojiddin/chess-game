from django.urls import path
from gaming.views import CountryListAPIView

app_name = 'gaming'

urlpatterns = [
    path('country', CountryListAPIView.as_view(), name='country-list')
]