# Generated by Django 4.2.7 on 2023-11-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchCountry', '0002_country_delete_worldborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='fips',
            field=models.CharField(max_length=2, null=True, verbose_name='FIPS Code'),
        ),
    ]
