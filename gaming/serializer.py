from rest_framework import serializers
from gaming.models import Country, Player


class CountryListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Country
		fields = ['id', 'name', 'prefix']


class PlayerListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Player
		fields = ['id', 'name', 'country', 'elo_rating', 'wins', 'losses', 'draws', 'games_played']


class PlayerAddSerializer(serializers.ModelSerializer):

	class Meta:
		model = Player
		fields = ['name', 'country', 'elo_rating', 'wins', 'losses', 'draws']


class PlayerUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Player
		fields = ['name', 'elo_rating', 'wins', 'losses', 'draws']


