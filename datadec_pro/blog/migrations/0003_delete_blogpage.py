# Generated by Django 5.0.4 on 2024-04-29 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_delete_blogindexpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
