# Generated by Django 5.0.6 on 2024-07-07 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_commentpage'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentPage',
            new_name='NotePage',
        ),
    ]