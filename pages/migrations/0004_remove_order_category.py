# Generated by Django 3.2 on 2021-09-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
    ]