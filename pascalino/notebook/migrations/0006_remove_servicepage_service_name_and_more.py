# Generated by Django 5.0.6 on 2024-07-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_servicepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepage',
            name='service_name',
        ),
        migrations.AlterField(
            model_name='hostpage',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
