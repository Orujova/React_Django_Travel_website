# Generated by Django 3.2 on 2023-08-16 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]