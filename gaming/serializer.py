from rest_framework import serializers
from gaming.models import Country, Player


class CountryListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Country
		fields = ['id', 'name', 'prefix']


class PlayerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Player
		fields = ['id', 'name', 'country', 'wins', 'losses', 'draws', 'games_played']