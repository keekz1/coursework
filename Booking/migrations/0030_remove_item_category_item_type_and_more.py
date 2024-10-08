# Generated by Django 5.0.3 on 2024-05-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0029_category_remove_item_type_alter_item_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
