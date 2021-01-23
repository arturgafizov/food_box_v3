import requests
from django.core.management.base import BaseCommand
from urllib.request import urlretrieve
from django.core.exceptions import ValidationError

from items.models import Item




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_item = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
        foods = link_item.json()


        for food in foods:

            item = Item.objects.filter(id=food['id']).first()
            name_image = food['image'].split('/')[-1]
            urlretrieve(food['image'], '/home/artyr/PycharmProjects/food_box_v3/food_box/media/item_images/' + name_image)  # через  + объединил путь и переменную
            try:
                d={}
                d['title'] = food['title']
                d['description'] = food['description']
                d['image'] = '/media/item_images/' + food['image'].split('/')[-1]
                d['weight'] = food['weight_grams']
                d['price'] = food['price']

                new_item = Item.objects.update_or_create(defaults=d, id=food['id'])

                self.stdout.write("Item successfully updated or created")

            except ValidationError:
                print("Validation Error")
            #if item:
            #    item.save()
            #    self.stdout.write("Item successfully updated")
            #if not item:
            #    new_item = Item.objects.create(
            #        title=food['title'],
            #        description=food['description'],
            #        image='/media/item_images/' + food['image'].split('/')[-1],
            #        weight=food['weight_grams'],
            #        price=food['price'])

            #    self.stdout.write("Item successfully created")
