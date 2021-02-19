import random
from rest_framework import response, status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from items.models import Item


class ItemListTestCase(APITestCase):
    def setUp(self) -> None:
        self.items = [
            Item.objects.create(title=f'title {b}', description=f'description {b}', image=None,
                                weight=random.randint(1000, 2000),
                                price=format(100, '.2f')) for b in range(10)
        ]

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('items:items-list')
        cls.item_data = {
            'title': 'Микс фрукт',
            'description': 'Десять видов сухофруктов и орехов',
            "image": None,
            'weight': '2000',
            'price': "200,00",
        }

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(
            data['results'],
            [
                {
                    'id': item.id,
                    'title': item.title,
                    'description': item.description,
                    'image': None,
                    'weight': item.weight,
                    'price': item.price
                }for item in self.items[:len(data['results'])]
            ]

        )
