# Generated by Django 5.0.3 on 2024-05-18 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0031_alter_todolist_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='lists',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='saveditem',
            old_name='lists',
            new_name='category',
        ),
    ]
