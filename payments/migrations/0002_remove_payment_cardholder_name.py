# Generated by Django 3.2 on 2023-08-02 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='cardholder_name',
        ),
    ]
