# Generated by Django 3.2.10 on 2021-12-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0002_exampleschild"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleM2M",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("has_many", models.ManyToManyField(to="test_app.Example")),
            ],
        ),
    ]