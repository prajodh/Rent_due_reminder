# Generated by Django 4.0 on 2021-12-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_rem',
            name='tmessage',
            field=models.CharField(max_length=300),
        ),
    ]
