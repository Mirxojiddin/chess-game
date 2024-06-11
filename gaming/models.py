
from django.db import models

from gaming.utilts import validate_isalpha, validate_non_negative


class Country(models.Model):
	name = models.CharField(max_length=50, validators=[validate_isalpha])
	prefix = models.CharField(max_length=5, validators=[validate_isalpha])

	def __str__(self):
		return f"{self.name}"

	class Meta:
		ordering = ['name']


class Player(models.Model):
	name = models.CharField(max_length=100, validators=[validate_isalpha])
	elo_rating = models.PositiveIntegerField(default=0, validators=[validate_non_negative])
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	wins = models.PositiveIntegerField(default=0, validators=[validate_non_negative])
	losses = models.PositiveIntegerField(default=0, validators=[validate_non_negative])
	draws = models.PositiveIntegerField(default=0, validators=[validate_non_negative])
	games_played = models.PositiveIntegerField(default=0, editable=False)

	def __str__(self):
		return f"{self.country.prefix} {self.name}"

	def save(self, *args, **kwargs):
		self.games_played = self.wins + self.losses + self.draws
		super(Player, self).save(*args, **kwargs)
