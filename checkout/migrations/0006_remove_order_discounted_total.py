# Generated by Django 3.2.6 on 2021-08-25 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_discounted_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discounted_total',
        ),
    ]