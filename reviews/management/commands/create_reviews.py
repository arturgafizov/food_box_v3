import requests
from django.core.management.base import BaseCommand
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from reviews.models import Rewiew

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_review = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json')
        reviews = link_review.json()
        #print(reviews)
        for review in reviews:
            try:
                #customer_review = Rewiew.objects.filter(id=review['id']).first()
                d={}
                d['text'] = review['content']
                d['created_at'] = review['created_at ']
                d['published_at'] = review['published_at']
                d['status'] = review['status']
                d['author_id'] = review['author']


                new_customer_review = Rewiew.objects.update_or_create(defaults=d, id=review['id'])

                self.stdout.write("Review successfully created or update")
            except ValidationError:
                print("Validation Error")

