# Generated by Django 4.1.4 on 2023-03-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spotify", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spotifytoken",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
