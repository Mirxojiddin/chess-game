from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

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


class CountryTestCase(APITestCase):
	def setUp(self):
		Country.objects.create(name="Uzbeksitan", prefix="uzb")

	def test_list_country(self):
		url = reverse('gaming:country-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		for data in response.data:
			self.assertEqual(list(data.keys()), ['id', 'name', 'prefix'])
		self.assertEqual(response.data[0]['id'], 1)
		self.assertEqual(response.data[0]['name'], "Uzbeksitan")
		self.assertEqual(response.data[0]['prefix'], 'uzb')

	def test_order_by_country(self):
		Country.objects.create(name="England", prefix="eng")
		url = reverse('gaming:country-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		for data in response.data:
			self.assertEqual(list(data.keys()), ['id', 'name', 'prefix'])
		self.assertEqual(response.data[0]['name'], "England")
		self.assertEqual(response.data[0]['prefix'], 'eng')
		self.assertEqual(response.data[1]['name'], "Uzbeksitan")
		self.assertEqual(response.data[1]['prefix'], 'uzb')

