# Generated by Django 4.2.8 on 2023-12-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="image", new_name="images",
        ),
    ]
