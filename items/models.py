from django.db import models
from rest_framework.serializers import ModelSerializer


# Create your models here.
from food_box.settings import MEDIA_ITEM_IMAGE_DIR



class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=MEDIA_ITEM_IMAGE_DIR)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


