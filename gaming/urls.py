from django.urls import path
from gaming.views import CountryListAPIView, PlayerListAPIView, PlayerDetailAPIView

app_name = 'gaming'

urlpatterns = [
    path('country', CountryListAPIView.as_view(), name='country-list'),
    path('player', PlayerListAPIView.as_view(), name='player'),
    path('player/<int:pk>', PlayerDetailAPIView.as_view(), name='player-detail')
]
