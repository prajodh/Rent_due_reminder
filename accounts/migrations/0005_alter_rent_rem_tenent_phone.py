# Generated by Django 4.0 on 2022-01-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_rent_rem_tenent_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_rem',
            name='tenent_phone',
            field=models.IntegerField(),
        ),
    ]