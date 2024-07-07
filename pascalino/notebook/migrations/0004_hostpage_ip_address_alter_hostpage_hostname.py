# Generated by Django 5.0.6 on 2024-07-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_hostpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostpage',
            name='ip_address',
            field=models.TextField(default='0.0.0.0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hostpage',
            name='hostname',
            field=models.TextField(blank=True),
        ),
    ]
