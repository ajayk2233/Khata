# Generated by Django 3.0.5 on 2020-04-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200429_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='desc',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
