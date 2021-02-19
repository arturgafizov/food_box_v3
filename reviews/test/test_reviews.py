import random
from rest_framework import response, status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from reviews.models import Review
from users.models import User


class ReviewViewSetListTestCase(APITestCase):
    def setUp(self) -> None:
        g = User.objects.create()
        self.reviews = [
            Review.objects.create(author=g, text=f'test {b}',
                                  created_at='2020-04-15 00:00:00',
                                  published_at='2020-04-15 00:00:00',
                                  status='published') for b in range(10)
        ]


    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('reviews:reviews-list')
        cls.review_data = {
            'author': 'lola999',
            'text': 'Good',
            'created_at': '2020-04-15 00:00:00',
            'published_at': '2020-04-15 00:00:00',
            'status': 'published',
        }

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(
            data['results'],
            [
                {
                    'id': review.id,
                    'author':  review.author_id,
                    'text': review.text,
                    'created_at': review.created_at,
                    'published_at': review.published_at,
                    'status': review.status,
                }for review in self.reviews[:len(data['results'])]
            ]

        )


class ReviewViewSetCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create()


    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('reviews:reviews-list')
        cls.review_data = {
            'author': 'lola999',
            'text': 'Good',
            'created_at': '2020-04-15 00:00:00',
            'published_at': '2020-04-15 00:00:00',
            'status': 'published',
        }

    # def test_unauthorized(self):
    #     response = self.client.post(self.url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})

    def test(self):
        data = {
            **self.review_data
        }
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, data=data)
        review = Review.objects.get()
        self.assertEqual(
            response.json(),
            {
                'id': review.id,
                'author':  review.author,
                'text': review.text,
                'created_at': review.created_at,
                'published_at': review.published_at,
                'status': review.status,
            },
        )
