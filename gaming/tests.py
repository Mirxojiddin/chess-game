from django.test import TestCase
from gaming.models import Country, Player


class PlayerTestCase(TestCase):
	def test_add_user(self):
		country = Country.objects.create(name="Uzbeksitan", prefix="uzb")
		Player.objects.create(name="Mirxojiddin",country=country, wins=10, losses=5, draws=8, elo_rating=1400)
		player = Player.objects.get(id=1)
		self.assertEqual(player.name, 'Mirxojiddin')
		self.assertEqual(player.country.name, 'Uzbeksitan')
		self.assertEqual(player.wins, 10)
		self.assertEqual(player.losses, 5)
		self.assertEqual(player.draws, 8)
		self.assertEqual(player.elo_rating, 1400)
		self.assertEqual(player.games_played, 23)

		player.wins = 8
		player.save()
		player = Player.objects.get(id=1)
		self.assertEqual(player.name, 'Mirxojiddin')
		self.assertEqual(player.country.name, 'Uzbeksitan')
		self.assertEqual(player.wins, 8)
		self.assertEqual(player.losses, 5)
		self.assertEqual(player.draws, 8)
		self.assertEqual(player.elo_rating, 1400)
		self.assertEqual(player.games_played, 21)

