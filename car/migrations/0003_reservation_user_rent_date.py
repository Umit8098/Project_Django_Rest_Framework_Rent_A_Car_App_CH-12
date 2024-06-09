# Generated by Django 5.0.6 on 2024-05-27 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_reservation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('customer', 'start_date', 'end_date'), name='user_rent_date'),
        ),
    ]
