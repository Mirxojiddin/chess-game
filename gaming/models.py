
from django.db import models


class Country(models.Model):
	name = models.CharField(max_length=50 )
	prefix = models.CharField(max_length=5)

	def __str__(self):
		return f"{self.name}"

	class Meta:
		ordering = ['name']


class Player(models.Model):
	name = models.CharField(max_length=100)
	elo_rating = models.PositiveIntegerField(default=0)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	wins = models.PositiveIntegerField(default=0)
	losses = models.PositiveIntegerField(default=0)
	draws = models.PositiveIntegerField(default=0)
	games_played = models.PositiveIntegerField(default=0, editable=False)

	def __str__(self):
		return f"{self.country.prefix} {self.name}"

	def save(self, *args, **kwargs):
		self.games_played = self.wins + self.losses + self.draws
		super(Player, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-elo_rating']
