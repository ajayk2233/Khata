# Generated by Django 3.0.5 on 2020-04-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200430_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='total_bal',
            field=models.IntegerField(default=0),
        ),
    ]
