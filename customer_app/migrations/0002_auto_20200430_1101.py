# Generated by Django 3.0.5 on 2020-04-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
