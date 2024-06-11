from rest_framework.generics import ListAPIView
from gaming.models import Country, Player
from gaming.serializer import PlayerListSerializer, CountryListSerializer


class CountryListAPIView(ListAPIView):
	queryset = Country.objects.all()
	serializer_class = CountryListSerializer

