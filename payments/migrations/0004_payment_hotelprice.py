# Generated by Django 3.2 on 2023-08-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='hotelprice',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
