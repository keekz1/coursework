# Generated by Django 5.0.3 on 2024-05-02 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0025_alter_bookingitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='unsaveditem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Booking.category'),
        ),
    ]
