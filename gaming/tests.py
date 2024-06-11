from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from gaming.models import Country, Player


class PlayerTestCase(TestCase):
	def setUp(self):
		country = Country.objects.create(name="Uzbeksitan", prefix="uzb")
		Player.objects.create(name="Mirxojiddin", country=country, wins=10, losses=5, draws=8, elo_rating=1400)

	def test_add_player_db(self):
		player = Player.objects.get(name="Mirxojiddin")
		self.assertEqual(player.name, 'Mirxojiddin')
		self.assertEqual(player.country.name, 'Uzbeksitan')
		self.assertEqual(player.wins, 10)
		self.assertEqual(player.losses, 5)
		self.assertEqual(player.draws, 8)
		self.assertEqual(player.elo_rating, 1400)
		self.assertEqual(player.games_played, 23)

		player.wins = 8
		player.save()
		player = Player.objects.get(name="Mirxojiddin")
		self.assertEqual(player.name, 'Mirxojiddin')
		self.assertEqual(player.country.name, 'Uzbeksitan')
		self.assertEqual(player.wins, 8)
		self.assertEqual(player.losses, 5)
		self.assertEqual(player.draws, 8)
		self.assertEqual(player.elo_rating, 1400)
		self.assertEqual(player.games_played, 21)

	def test_list_player(self):
		url = reverse('gaming:player')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		for data in response.data:
			self.assertEqual(
				list(data.keys()),
				['id', 'name', 'country', 'elo_rating', 'wins', 'losses', 'draws', 'games_played']
			)
		self.assertEqual(response.data[0]['wins'], 10)
		self.assertEqual(response.data[0]['losses'], 5)
		self.assertEqual(response.data[0]['draws'], 8)
		self.assertEqual(response.data[0]['name'], 'Mirxojiddin')
		self.assertEqual(response.data[0]['elo_rating'], 1400)
		self.assertEqual(response.data[0]['games_played'], 23)
		country = Country.objects.get(name="Uzbeksitan")
		Player.objects.create(name="Nurali", country=country, wins=45, losses=52, draws=9, elo_rating=2000)
		response = self.client.get(url)
		for data in response.data:
			self.assertEqual(
							list(data.keys()),
							['id', 'name', 'country', 'elo_rating', 'wins', 'losses', 'draws', 'games_played']
			)
		self.assertEqual(response.data[0]['wins'], 45)
		self.assertEqual(response.data[0]['losses'], 52)
		self.assertEqual(response.data[0]['draws'], 9)
		self.assertEqual(response.data[0]['name'], 'Nurali')
		self.assertEqual(response.data[0]['elo_rating'], 2000)
		self.assertEqual(response.data[0]['games_played'], 106)
		self.assertEqual(response.data[1]['wins'], 10)
		self.assertEqual(response.data[1]['losses'], 5)
		self.assertEqual(response.data[1]['draws'], 8)
		self.assertEqual(response.data[1]['name'], 'Mirxojiddin')
		self.assertEqual(response.data[1]['elo_rating'], 1400)
		self.assertEqual(response.data[1]['games_played'], 23)

	def test_add_player(self):
		url = reverse('gaming:player')
		country = Country.objects.get(name="Uzbeksitan")
		payload = {
			"name": "Nurali",
			"country": country.id,
			"elo_rating": 3000,
			"wins": 10,
			"losses": 12,
			"draws": 16
		}

		response = self.client.post(url, data=payload)
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.data['wins'], 10)
		self.assertEqual(response.data['losses'], 12)
		self.assertEqual(response.data['draws'], 16)
		self.assertEqual(response.data['name'], 'Nurali')
		self.assertEqual(response.data['elo_rating'], 3000)
		url = reverse('gaming:player')
		response = self.client.get(url)
		for data in response.data:
			self.assertEqual(
							list(data.keys()),
							['id', 'name', 'country', 'elo_rating', 'wins', 'losses', 'draws', 'games_played']
			)
		self.assertEqual(response.data[0]['wins'], 10)
		self.assertEqual(response.data[0]['losses'], 12)
		self.assertEqual(response.data[0]['draws'], 16)
		self.assertEqual(response.data[0]['name'], 'Nurali')
		self.assertEqual(response.data[0]['elo_rating'], 3000)
		self.assertEqual(response.data[0]['games_played'], 38)
		self.assertEqual(response.data[1]['wins'], 10)
		self.assertEqual(response.data[1]['losses'], 5)
		self.assertEqual(response.data[1]['draws'], 8)
		self.assertEqual(response.data[1]['name'], 'Mirxojiddin')
		self.assertEqual(response.data[1]['elo_rating'], 1400)
		self.assertEqual(response.data[1]['games_played'], 23)

	def test_add_player_error(self):
		url = reverse('gaming:player')
		country = Country.objects.get(name="Uzbeksitan")
		payload = {
			"country": country.id,
			"elo_rating": 3000,
			"wins": 10,
			"losses": 12,
			"draws": 16
		}
		response = self.client.post(url, data=payload)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.json()['name'], ['This field is required.'])
		payload = {
			"name":"tojiddin",
			"country": country.id,
			"elo_rating": -3000,
			"wins": -10,
			"losses": 12,
			"draws": 16
		}
		response = self.client.post(url, data=payload)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.json()['elo_rating'], ["Ensure this value is greater than or equal to 0."])
		self.assertEqual(response.json()['wins'], ["Ensure this value is greater than or equal to 0."])

	def test_get_player(self):
		player = Player.objects.get(name="Mirxojiddin")
		url = reverse('gaming:player-detail', kwargs={'pk':player.id})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['wins'], 10)
		self.assertEqual(response.data['losses'], 5)
		self.assertEqual(response.data['draws'], 8)
		self.assertEqual(response.data['name'], 'Mirxojiddin')
		self.assertEqual(response.data['elo_rating'], 1400)
		self.assertEqual(response.data['games_played'], 23)

	def test_edit_player(self):
		player = Player.objects.get(name="Mirxojiddin")
		payload = {
			"name": "tojiddin",
			"elo_rating": 1200,
			"wins": 20,
			"losses": 12,
			"draws": 16
		}
		url = reverse('gaming:player-detail', kwargs={'pk': player.id})
		response = self.client.put(url, data=payload, content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['wins'], 20)
		self.assertEqual(response.data['losses'], 12)
		self.assertEqual(response.data['draws'], 16)
		self.assertEqual(response.data['name'], 'tojiddin')
		self.assertEqual(response.data['elo_rating'], 1200)
		payload = {
			"name": "Mirxojiddin",
			"losses": 20,
			"draws": 16
		}
		response = self.client.patch(url, data=payload, content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['wins'], 20)
		self.assertEqual(response.data['losses'], 20)
		self.assertEqual(response.data['draws'], 16)
		self.assertEqual(response.data['name'], 'Mirxojiddin')
		self.assertEqual(response.data['elo_rating'], 1200)


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
