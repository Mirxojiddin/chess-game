from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from gaming.models import Country, Player
from gaming.serializer import PlayerListSerializer, CountryListSerializer, PlayerAddSerializer, PlayerUpdateSerializer


class CountryListAPIView(ListAPIView):
	queryset = Country.objects.all()
	serializer_class = CountryListSerializer


class PlayerListAPIView(ListAPIView, CreateAPIView):
	queryset = Player.objects.all()

	def get_serializer_class(self):
		if self.request.method == "GET":
			return PlayerListSerializer
		else:
			return PlayerAddSerializer


class PlayerDetailAPIView(DestroyAPIView, RetrieveAPIView, UpdateAPIView):
	queryset = Player.objects.all()
	lookup_field = "pk"

	def get_serializer_class(self):
		if self.request.method == "PUT" or self.request.method == "PATCH":
			return PlayerUpdateSerializer
		else:
			return PlayerListSerializer
