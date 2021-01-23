# Generated by Django 3.0.7 on 2021-01-14 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_auto_20210114_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiew',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewiews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rewiew',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rewiew',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
